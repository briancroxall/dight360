#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:20:26 2018

@author: briancroxall
"""

import sys

for each in sys.argv[1:]:
    with open(each) as my_file:
        print(each, my_file.read().count('print('), sep='\t')