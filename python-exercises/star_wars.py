#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:29:30 2018

@author: briancroxall
"""

import json
from pprint import pprint
import requests as r

def get_swapi(url):
    """Get json data from StarWars API; return dict."""
    # Star Wars API (does not require authentication)
    response = r.get(url)
    return json.loads(response.text)


luke = get_swapi('https://swapi.co/api/people/1/')
print('This is the dict (not pretty printed):', luke)
print('Here is the name:', luke['name'])

for ship_url in luke['starships']:
    ship = get_swapi(ship_url)
    pprint(ship)