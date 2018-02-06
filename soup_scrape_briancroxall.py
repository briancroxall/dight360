#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:11:28 2018

@author: briancroxall

Assignment: 
Write a function called `get_rnlp` that requests an arbitrary filename
(filename is an argument of the function) from
`http://reynoldsnlp.com/scrape/` and saves the file in the local folder
`scrape/`. (If you give the argument "aa.html", it should get the HTML from
"http://reynoldsnlp.com/scrape/aa.html".)

Write a function called `get_hrefs` that opens a local html file (filename
is an argument of the function), parses it using `BeautifulSoup` and returns
a list of href values for all <a> tags in the file. (If you give the argument
"aa.html", it should get the HTML from the local file "scrape/aa.html" and
return a list of hrefs.)

The two functions above will be used for the following. Write a loop that
will iteratively request a url, parse it, extract the hrefs, and then do the
same thing with all of those hrefs. Begin with 'aa.html'.

"""
from bs4 import BeautifulSoup
import re
import random
import requests as r
import time

headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}  # noqa: E501 identify self
reynolds = 'http://reynoldsnlp.com/scrape/aa.html'  

"""
for page in reynolds:  
    response = r.get(wikipedia + term, headers=headers1)
    time.sleep(random.uniform(1.5, 2.5))  # give the server some rest
    with open(term + '.html', 'w') as my_file:  # noqa: E501 open file in write mode, using name of query
        print(response.text, file=my_file)
"""
# Scrape one page
response = r.get(reynolds, headers=headers1)
time.sleep(random.uniform(1.5, 2.5))
with open('scrape/aa' + '.html', 'w') as my_file:
    print(response.text, file=my_file)
print('Success!')
print()  
    
# Parse one file
with open('scrape/aa.html') as aa_file:
    soup = BeautifulSoup(aa_file, 'html.parser')
print(soup.prettify())
"""
def get_rnlp    
    
def get_hrefs:
    

    
    list comprehensions
sent1 = 'This is an example sentence.'.split()
[word for word in sent1 if 'a' in word]

    
for
""" 