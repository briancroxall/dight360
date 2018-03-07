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

def get_crime(url):
    """Get json data from StarWars API; return dict."""
    # Star Wars API (does not require authentication)
    response = r.get(url)
    sleep(random.uniform(1.5, 2.5))
    return json.loads(response.text)


feb = get_crime('https://data.police.uk/api/crime-categories?date=2018-02')
print(feb)
