#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:18:10 2018

@author: briancroxall
"""

import nltk
from nltk.probability import FreqDist
from glob import glob
import re
from string import punctuation as p

def clean(words):
    # Function to clean out the metadata, tags, and headers
    clean_re = r'<p>(.*)'  # noqa: E501 regex to find text within <p> tags only. Didn't take header text
    clean_text = re.findall(clean_re, words)  # noqa: E501 use findall to get text and assign it
    join_clean = ' '.join(clean_text)  # noqa: E501 what findall returns is a list of strings, so those strings need to be joined again
    return join_clean

with open('Mini-CORE/1+IN+EN+IN-IN-IN-IN+EN-EN-EN-EN+WIKI+9992596.txt', 'r') as my_file:  # noqa: E501
    text = my_file.read().lower()
    clean_text = clean(text)
    tokens = nltk.word_tokenize(clean_text)
    tokens_fd = FreqDist(tokens)
    print(tokens[0:5])
    print(tokens_fd)
    