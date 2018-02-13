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
    
Select 3 linguistic features that you think will vary across register 
categories.
Identify those features (make sure to check accuracy)
Calculate normed rates of occurrence (per 1,000 words)
Print them to a tab-separated file along with a column for 'Register' which
should contain a single two letter code for the register category (i.e. 
extract the two letter register code from the filename). Your output should 
be 1601 lines long and should look something like:
    
filename	<feat1>	<feat2>	<feat3>	register
1+IN+....txt	15.2	131.3	22.4	IN
1+HI+....txt	14.6	119.6	26.9	HI
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
from glob import glob

"""
file = 'Mini-CORE/1+IN+EN+IN-IN-IN-IN+EN-EN-EN-EN+WIKI+9992596.txt'
short_file = file.split('/').pop()
prefix = short_file.split('+')
genre = prefix[1]
print(genre)
"""

def extract_genre(filename):
    """ Function to extract genre from file name """
    short_file = filename.split('/').pop()  # splits the file name on slashes and keeps the last part and saves it to the variable
    prefix = short_file.split('+')  # splits the file on the pluses and saves the list to the variable
    register = prefix[1]  # takes the 1th index of the list, which is what I needed, and saves it to the variable
    return register  # returns the genre



with open('output.tsv', 'w') as my_file: # opens file to start writing
    print('filename', 'feat1', 'feat2', 'feat3', 'register', sep='\t', file=my_file)  # noqa: E501 prints the headers, separated by tabs
    for each in glob('Mini-CORE/*.txt'):  # for loop to iterate over corpus
        print(each, '', '', '', extract_genre(each), sep='\t', file=my_file)  # noqa: E501 write t
    




"""
for filename in glob('Mini-CORE/*.txt'):
    with open(filename, 'r') as f:
        print


"""     
        
"""       
print('Text', 'TTR', 'artTR', 'smoteTR', sep='\t')
for t in [text1, text2, text3, text4]:
    print(t.name, ttr(t), artTR(t), smoteTR(t), sep='\t')
"""