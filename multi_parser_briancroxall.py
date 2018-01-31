#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment: In this script, open the file and pseudo-parse it with a regular
expression to extract the information you are interested in. Save that
information in another file (<filename>_parsed.txt).

Created on Tue Jan 30 18:28:10 2018

@author: briancroxall

Code to open file, parse with RegEx to find mascot name, school population
size, and geo coordinates, and output to new file. 
Attempting to run on multiple files.
"""
from glob import glob
import re #regular expressions 

# open and read multiple files
for filename in glob('*.html'):
    with open(filename, 'r') as my_file:
        text = my_file.read()

# Find mascots
mascots_re = r'Nickname</a></th>\n<td>(.*?)</td>' #regex query
print('regex for mascots:', mascots_re) #display the regex string in the console #noqa: E501
result_mascot = re.findall(mascots_re, text, re.I) #run query with findall
with open(filename + '.txt', 'w') as my_file1:
    print('Mascot: ', result_mascot, file = my_file1) #save results to new file
print('re.findall():', result_mascot) # print results to console
print()

#Find population 
population_re = r'Enrollment</th>\n<td>(.*?)<'
print('regex for population:', population_re)
result_population = re.findall(population_re, text, re.I)
with open(filename + '.txt', 'a') as my_file2:
    print('School population:', result_population, file = my_file2)
print('re.findall():', result_population)
print()

#Find coordinates
geo_re = r'span class="geo">(.*?)</span'
print('regex for coordinates:', geo_re)
result_geo = re.findall(geo_re, text, re.I)
with open(filename + '.txt', 'a') as my_file3:
    print('Coordinates:', result_geo, file = my_file3)
print('re.findall():', result_geo)
print()

"""
from glob import glob

for filename in glob('*.py'):
    print(filename)
"""