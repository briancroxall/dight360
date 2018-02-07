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


Code for a single site implementation as a first pass.

"""
from bs4 import BeautifulSoup
import random
import requests as r
import time

headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}  # noqa: E501 identify self
reynolds = 'http://reynoldsnlp.com/scrape/'  



# Scrape one page
response = r.get(reynolds, headers=headers1)
time.sleep(random.uniform(1.5, 2.5))
with open('scrape/aa' + '.html', 'w') as my_file:
    print(response.text, file=my_file)
print('Success!')
print()  
    
# Parse one file
sites = []
with open('scrape/aa.html') as aa_file:
    soup = BeautifulSoup(aa_file, 'html.parser')
for link in soup.find_all('a'):
    print('link type', type(link))
    
    url = link.get('href')
    end = url.split('/')[-1]
    sites.append(end)
print(sites)

