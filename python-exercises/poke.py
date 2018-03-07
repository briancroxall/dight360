#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:29:30 2018

@author: briancroxall
"""

import json
from pprint import pprint
import requests as r
from time import sleep
import random

def get_poke_api(url):
    """Get json data from Pokemon API; return dict."""
    # Star Wars API (does not require authentication)
    response = r.get(url)
    print(response.text)
    sleep(random.uniform(1.5, 2.5))
    return json.loads(response.text)

for i in range(1,11):
    str_ = str(i)
    url = 'http://pokeapi.co/api/v2/pokemon/' + str_ + '/'
    print(url)
    poke = get_poke_api(url)
    print('Here is the name:', poke['name'])


"""
bulba = get_poke_api('http://pokeapi.co/api/v2/pokemon/1/')
print('This is the dict (not pretty printed):', bulba)
print('Here is the name:', bulba['name'])

types = []
for type_ in bulba['types']:
    types.extend(type_)
print(types)


"""
"""
print('Here is the type:', bulba['types'])

"""
"""
for ship_url in luke['starships']:
    ship = get_swapi(ship_url)
    pprint(ship)
    
"""