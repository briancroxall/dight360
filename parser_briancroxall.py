#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment: In this script, open the file and pseudo-parse it with a regular
expression to extract the information you are interested in. Save that
information in another file (<filename>_parsed.txt).

Created on Tue Jan 30 18:28:10 2018

@author: briancroxall

Code to open file, parse with RegEx to find mascot name and school population
size, and output to new file.
"""
import re

# open file. 
redlands = open('redlands+high+school.html', 'r') #I'm currently calling a single file. I need to somehow iterate over the files I've scraped.
"""
print(redlands) # this just seems to print the file name, or rather the TextIOWrapper and mode. So that leads me to think that this isn't what I want.
"""

"""
for line in redlands:
    print(line) # This prints the whole file to the console. 
"""

# Find mascots
mascots_re = r'Nickname</a></th>\n<td>(.*?)</td>' #regex query
print('regex for mascots:', mascots_re) #display the regex string in the console #noqa: E501
result_mascot = re.findall(mascots_re, redlands, re.I) #run query with findall
with open('redlands_parsed.txt', 'w') as my_file:
    print('Mascot: ' + result_mascot, file = my_file) #save results to new file
print('re.findall():', result_mascot) # print results to console
print()

"""
#Find population 
population_re = r'Enrollment</th>\n<td>(.*?)<'
print('regex for population:', population_re)
result_population = re.findall(population_re, redlands, re.I)
with open('redlands_parsed.txt', 'a') as my_file2:
    print('School population:' + result_population, file = my_file2)
print('re.findall():', result_population)
print()
"""