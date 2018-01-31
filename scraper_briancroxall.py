#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment: Choose any website(s) that you would like to scrape 
and write a script to get the html and save it to a file (<filename>.html).

Code to scrape Wikipedia and save output to files.

Created on Mon Jan 29 15:08:47 2018

@author: briancroxall
"""
import random 
import requests as r
import time

headers1= {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'} #identify self
wikipedia = 'http://en.wikipedia.org/wiki/Special:Search?search=' # query url
for term in ['redlands+high+school', 'redlands+east+valley+high+school', 'citrus+valley+high+school']: #noqa E501
    response = r.get(wikipedia + term, headers=headers1)
    time.sleep(random.uniform(1.5, 2.5)) # give the server some rest
    with open(term + '.html', 'w') as my_file: # open file in write mode, using name of query
        print(response.text, file = my_file) # write contents of page to file opened in previous line





