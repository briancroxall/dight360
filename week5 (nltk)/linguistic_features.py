#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment:

IN: Informational (Wikipedia)

IP: Informational Persuasion

LY: Song Lyrics

NA: News reports

OP: Opinion blogs

SP: Interview transcripts

The filenames are long. You can ignore everything except the first two letter
code (after the 1+). That will tell you the register. For example,
1+IP+DS+IP-IP-IP-IP+DS-DS-DS-DS+NNNY+0583255.txt is an IP text.

Each file has a header with human annotator ratings and other information.
You should only include lines that begin with <h> or <p> in your analysis
(but remove the <h> or the <p>).
    
- Select 3 linguistic features that you think will vary across register 
categories.
- Identify those features (make sure to check accuracy)
- Calculate normed rates of occurrence (per 1,000 words)
- Print them to a tab-separated file along with a column for 'Register' which
should contain a single two letter code for the register category (i.e. 
extract the two letter register code from the filename). Your output should 
be 1601 lines long and should look something like:
    
filename    <feat1>    <feat2>    <feat3>    register
1+IN+....txt    15.2    131.3    22.4    IN
1+HI+....txt    14.6    119.6    26.9    HI
Change <feat1>, <feat2>, and <feat3> to actual labels of your selected 
features. Here are some features you can consider counting:

pronouns (all pronouns or 1st, 2nd, or 3rd)
proper nouns
past tense
modals
contractions
punctuation (e.g., ? or !)

Created on Mon Feb 12 15:27:45 2018

@author: briancroxall

"""

import nltk
from nltk.probability import FreqDist
from glob import glob
import re
from string import punctuation as p

"""
# test file block
with open('Mini-CORE/1+IN+EN+IN-IN-IN-IN+EN-EN-EN-EN+WIKI+9992596.txt', 'r') as my_file:  # noqa: E501
    text = my_file.read().lower()
    clean_re = r'<p>(.*)'
    clean_text = re.findall(clean_re, text)
    print(clean_text)

    
"""


def clean(words):
    # Function to clean out the metadata, tags, and headers
    clean_re = r'<p>(.*)'  # noqa: E501 regex to find text within <p> tags only. Didn't take header text
    clean_text = re.findall(clean_re, words)  # noqa: E501 use findall to get text and assign it
    join_clean = ' '.join(clean_text)  # noqa: E501 what findall returns is a list of strings, so those strings need to be joined again
    return join_clean

def pronouns(words):
    # Function to extract first-person, singular pronouns from corpus 
    pro_I = tokens_fd['i']  # noqa: E501 returns the int value for the key 'i' (AKA the number of times i appears as a single token)
    pro_me = tokens_fd['me']
    pro_my = tokens_fd['my']
    pro_mine = tokens_fd['mine']
    total_pronouns = pro_I + pro_me + pro_my + pro_mine  # noqa: E501 adds the totals of each pronoun together
    normed_first = total_pronouns / len(words)  # noqa: E501 divides the total pronouns by the total number of tokens
    return normed_first  # returns that total 

def punct(words):
    # Function to extract ! and ? from corpus
    punctq = tokens_fd['?']
    puncte = tokens_fd['!']
    total_excite = punctq + puncte
    normed_punct = total_excite / len(words)
    return normed_punct

def extract_genre(filename):
    # Function to extract genre from file name 
    short_file = filename.split('/').pop()  # noqa: E501 splits the file name on slashes and keeps the last part and saves it to the variable
    prefix = short_file.split('+')  # noqa: E501 splits the file on the pluses and saves the list to the variable
    register = prefix[1]  # noqa: E501 takes the 1th index of the list, which is what I needed, and saves it to the variable
    return register  # returns the genre

with open('output.tsv', 'w') as my_file: # opens file to start writing
    print('filename', 'singular first-person pronouns', 'Interrogative or Exclamation', 'Contractions', 'register', sep='\t', file=my_file)  # noqa: E501 prints the headers, separated by tabs
    for each in glob('Mini-CORE/*.txt'):   # for loop to iterate over corpus
       with open(each, 'r') as read_file:  # noqa: E501 read each file in the for-loop to prevent doing it multiple times in each different feature function
           text = read_file.read().lower()  # noqa: E501 opens the file, reads the file, and lowercases the file and saves it to the variable
           cleaned_text = clean(text)  # process text through clean function
           tokens = nltk.word_tokenize(cleaned_text)  # noqa: E501 tokenizes the file that had been saved to the variable
           tokens_fd = FreqDist(tokens)  # noqa: E501 takes the frequency distribution of the tokens
       print(each, pronouns(tokens_fd), punct(tokens_fd), '', extract_genre(each), sep='\t', file=my_file)  # noqa: E501 write the results of each text moving through each function to the outpt file
    



"""
re.search('[' + p + ']'), 'This is a test.').group(0))
   
      
print('Text', 'TTR', 'artTR', 'smoteTR', sep='\t')
for t in [text1, text2, text3, text4]:
    print(t.name, ttr(t), artTR(t), smoteTR(t), sep='\t')
"""