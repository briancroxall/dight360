#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:45:27 2018

@author: briancroxall
"""

import nltk
"""
print('### Tokenizing and `Text` objects')
raw_text = ('I\'ll bet you wish that you had come up with this sentence.'
            'Call me Dr. Brillant! Sir Robin\'s sentence was much worse.')
print(raw_text)
sents = nltk.sent_tokenize(raw_text)
print(sents)
tokens = nltk.word_tokenize(raw_text)
print(tokens)
my_text = nltk.Text(tokens)
print(dir(my_text))
print()
"""

print('Frequency distributions')

from nltk.probability import FreqDist

print('FreqDist of Batman theme song')
batman_fd = FreqDist(nltk.word_tokenize('na na na na na na na na na na na na na na na na Bat Man!'))
print(batman_fd.most_common(5))
print()
input()

print('How about words that only occur once? ("singletons" or "hapaxes")')
print(batman_fd.hapaxes())
print()
input()

print('What are the 50 most common words in Genesis?')
fd3 = FreqDist(text3)
print(fd3.most_common(50))
print()
input()

print('How frequent is "prayed" in Genesis?')
# FreqDist objects are sub-types of dict
print(fd3['prayed'])
print()


