#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:11:28 2018

@author: briancroxall

Assignment:
Write a function called `get_rnlp` that requests an arbitrary filename
(filename is an argument of the function) from
`http://reynoldsnlp.com/scrape/` and saves the file in the local folder
`scrape/`. (If you give the argument "aa.html", it should get the HTML from
"http://reynoldsnlp.com/scrape/aa.html".)

Write a function called `get_hrefs` that opens a local html file (filename
is an argument of the function), parses it using `BeautifulSoup` and returns
a list of href values for all <a> tags in the file. (If you give the argument
"aa.html", it should get the HTML from the local file "scrape/aa.html" and
return a list of hrefs.)

The two functions above will be used for the following. Write a loop that
will iteratively request a url, parse it, extract the hrefs, and then do the
same thing with all of those hrefs. Begin with 'aa.html'.

"""
from bs4 import BeautifulSoup
import random
import requests as r
import time


def get_rnlp(seed):

    """ This grabs a specified URL from Rob's site and saves it to a folder"""
    reynolds = 'http://reynoldsnlp.com/scrape/'  # stem for site
    headers1 = {'user-agent': 'Brian Croxall (brian.croxall@byu.edu)'}  # noqa: E501 identify self
    response = r.get(reynolds + seed, headers=headers1)
    time.sleep(random.uniform(1.5, 2.5))  # don't kill the server
    with open('scrape/' + seed, 'w') as my_file:  # open file
        print(response.text, file=my_file)  # write content of response to file
        print('Successfully scraped ' + seed)  # noqa: E501; prints a message so we know it worked
    print()  # blank line


def get_hrefs(filename):

    # Opens the file passed to it and parses for the other links on the page
    sites = []  # creates an empty list to add the URLs to
    with open('scrape/' + filename) as html_file:  # noqa: E501 opens the file passed to it
        soup = BeautifulSoup(html_file, 'html.parser')  # noqa: E501 creates variable soup that has the read content of the file via BS
    for link in soup.find_all('a'):  # finds all the a elements on the page
        # print('link type', type(link))  # noqa: E501 prints the type of all the a elements
        url = link.get('href')  # gets the value for all the href keys
        end = url.split('/')[-1]  # splits the value (a url) on its last slash
        sites.append(end)  # adds the end of the url to the empty list
    return sites  # prints the list to verify things worked correcrtly

site_list = ['aa.html']  # to-do list
done_list = []  # things that have been scrape already
while len(site_list) > 0:  # if to-do list isn't empty
    item = site_list.pop()  # pop the last item off the to-do list
    if item in done_list:  # check done list to see if the item is already there
        continue  # if it's in the done list, don't do anything BUT keep running the loop
    else:  # if it's NOT in the done list
        get_rnlp(item)  # runs first function on seed item
        sites = get_hrefs(item)  # runs second function on seed item
        site_list.extend(sites)  # noqa: E501 adds the list from the second function to the initial seed list
        done_list.append(item)  # add the item to the done list
