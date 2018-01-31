#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:10:24 2018

@author: briancroxall
"""

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def bad_delete_head(t):
    t = t[1:]
    
def tail(t):
    return t[1:]

def nested_sum_bc(list):  #didn't work, but keeping for records
    for i in list:
        sum(i)
    print(i)
  

def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
   
    t: list of list of numbers

    returns: number
    """
    total = 0
    for nested in t:
        total += sum(nested)
    return total      

def cumsum_bc(t):
    """Computes the cumulative sum of a list of numbers.
    
    t: list of numbers
    
    returns: number
    """
    total = 0
    for number in t:
        sum[number[0:1]]
    print(number)
    
def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers
    """
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

def middle(t):
    """Returns a new list that contains all but first and last elements.
    
    t: list
    
    returns: new list
    """
    res = []
    for items in t:
        res = t[1:-1]
    return res
        