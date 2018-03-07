#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:12:01 2018

@author: briancroxall
"""

import sys

filename = sys.argv[1]

with open(filename, 'w') as my_file:
    print('It worked!', file=my_file)
    
