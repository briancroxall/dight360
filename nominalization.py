#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:57:43 2018

@author: briancroxall
"""

'''
TEXT:

In a development that would have been hard to imagine a generation ago, when video games were poised to take over living rooms, board games are thriving. Overall, the latest available data shows that U.S. sales grew by 28 percent between the spring of 2016 and the spring of 2017. Revenues are expected to rise at a similar rate into the early 2020s—largely, says one analyst, because the target audience “has changed from children to adults,” particularly younger ones.

Much of this success is traceable to the rise of games that, well, get those adults acting somewhat more like children. Clever, low-overhead card games such as Cards Against Humanity, Secret Hitler, and Exploding Kittens (“A card game for people who are into kittens and explosions”) have sold exceptionally well. Games like these have proliferated on Kickstarter, where anyone with a great idea and a contact at an industrial printing company can circumvent the usual toy-and-retail gatekeepers who green-light new concepts. (The largest project category on Kickstarter is “Games,” and board games make up about three-quarters of those projects.)

Growth has also been particularly swift in the category of “hobby” board games, which comprises more sophisticated titles that are oriented toward older players—think Settlers of Catan. These games, compared to ones like Monopoly and Cards Against Humanity, represent a niche segment, but that segment is becoming something more than a niche: According to ICv2, a trade publication that covers board games, comic books, and other hobbyist products, sales of hobby board games in the U.S. and Canada increased from an estimated $75 million to $305 million between 2013 and 2016, the latest year for which data is available.

Hobby-game fanaticism is still very much a subculture, to be sure, but it is a growing one. At the 2017 iteration of Gen Con—North America’s largest hobby-gaming convention, in Indianapolis—turnstile attendance topped 200,000. For the first time in the event’s history, all the attendee badges were purchased before the event began. Whether they knew it or not, the many thousands of people carpeting the field level of Lucas Oil Stadium wouldn’t be there if it weren’t for a small group of obsessives on the other side of the Atlantic.

The rise of hobbyist games is legible in the career arc of one of the genre’s most famous present-day designers, Phil Eklund. He was born and raised in the United States. But tellingly, he didn’t really hit his stride until moving to Germany. Eklund took to game design early in life. As a teenager growing up in Tucson in the 1970s, he became frustrated with the narrow, child-oriented fare on offer at his local toy shops—roll-and-move games like Sorry! and Monopoly. So he started creating his own games, making photocopied print runs of a few hundred or so and mailing them out to customers.

'''

'''
Assignment:
    Use regular expressions and lists to correctly identify and count all of the nominalizations in a short text. 
    You can simply paste a short text into a variable in your script.
'''


a = 'In a development that would have been hard to imagine a generation ago, when video games were poised to take over living rooms, board games are thriving. Overall, the latest available data shows that U.S. sales grew by 28 percent between the spring of 2016 and the spring of 2017. Revenues are expected to rise at a similar rate into the early 2020s—largely, says one analyst, because the target audience “has changed from children to adults,” particularly younger ones. Much of this success is traceable to the rise of games that, well, get those adults acting somewhat more like children. Clever, low-overhead card games such as Cards Against Humanity, Secret Hitler, and Exploding Kittens (“A card game for people who are into kittens and explosions”) have sold exceptionally well. Games like these have proliferated on Kickstarter, where anyone with a great idea and a contact at an industrial printing company can circumvent the usual toy-and-retail gatekeepers who green-light new concepts. (The largest project category on Kickstarter is “Games,” and board games make up about three-quarters of those projects.) Growth has also been particularly swift in the category of “hobby” board games, which comprises more sophisticated titles that are oriented toward older players—think Settlers of Catan. These games, compared to ones like Monopoly and Cards Against Humanity, represent a niche segment, but that segment is becoming something more than a niche: According to ICv2, a trade publication that covers board games, comic books, and other hobbyist products, sales of hobby board games in the U.S. and Canada increased from an estimated $75 million to $305 million between 2013 and 2016, the latest year for which data is available. Hobby-game fanaticism is still very much a subculture, to be sure, but it is a growing one. At the 2017 iteration of Gen Con—North America’s largest hobby-gaming convention, in Indianapolis—turnstile attendance topped 200,000. For the first time in the event’s history, all the attendee badges were purchased before the event began. Whether they knew it or not, the many thousands of people carpeting the field level of Lucas Oil Stadium wouldn’t be there if it weren’t for a small group of obsessives on the other side of the Atlantic.'
print(a)