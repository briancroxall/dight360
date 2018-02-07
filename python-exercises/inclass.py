#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:45:31 2018

@author: briancroxall
"""


"""
for i in range(3):
    with open('file' + str(i) + '.txt', 'a') as my_file:
        print('This is file', i, '.txt.')
"""


for i in range(3):
    with open('file' +str(i) + '.txt', 'w') as banana:
        print('This is file' + str(i) + '.txt', file = banana)
        