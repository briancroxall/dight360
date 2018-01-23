#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment:
    Use regular expressions and lists to correctly identify and
    count all of the nominalizations in a short text.
    You can simply paste a short text into a variable in your script.
"""
import re

'''
TEXT:

Thomas Alva Edison (February 11, 1847 – October 18, 1931) was an American
inventor and businessman, who has been described as America's greatest
inventor. He developed many devices that greatly influenced life around the
world, including the phonograph, the motion picture camera, and the
long-lasting, practical electric light bulb. Dubbed "The Wizard of Menlo
Park", he was one of the first inventors to apply the principles of mass
production and large-scale teamwork to the process of invention, and because
of that, he is often credited with the creation of the first industrial
research laboratory.

Edison was a prolific inventor, holding 1,093 US patents in his name, as well
as many patents in the United Kingdom, France, and Germany. More significant
than the number of Edison's patents was the widespread impact of his
inventions: electric light and power utilities, sound recording, and motion
pictures all established major new industries worldwide. Edison's inventions
contributed to mass communication and, in particular, telecommunications.
These included a stock ticker, a mechanical vote recorder, a battery for an
electric car, electrical power, recorded music and motion pictures. His
advanced work in these fields was an outgrowth of his early career as a
telegraph operator. Edison developed a system of electric-power generation
and distribution to homes, businesses, and factories – a crucial development
in the modern industrialized world. His first power station was on Pearl
Street in Manhattan, New York.

'''

words = 'Thomas Alva Edison (February 11, 1847 – October 18, 1931) was an American inventor and businessman, who has been described as America\'s greatest inventor. He developed many devices that greatly influenced life around the world, including the phonograph, the motion picture camera, and the long-lasting, practical electric light bulb. Dubbed "The Wizard of Menlo Park", he was one of the first inventors to apply the principles of mass production and large-scale teamwork to the process of invention, and because of that, he is often credited with the creation of the first industrial research laboratory. Edison was a prolific inventor, holding 1,093 US patents in his name, as well as many patents in the United Kingdom, France, and Germany. More significant than the number of Edison\'s patents was the widespread impact of his inventions: electric light and power utilities, sound recording, and motion pictures all established major new industries worldwide. Edison\'s inventions contributed to mass communication and, in particular, telecommunications. These included a stock ticker, a mechanical vote recorder, a battery for an electric car, electrical power, recorded music and motion pictures. His advanced work in these fields was an outgrowth of his early career as a telegraph operator. Edison developed a system of electric-power generation and distribution to homes, businesses, and factories – a crucial development in the modern industrialized world. His first power station was on Pearl Street in Manhattan, New York.'  # noqa: E501
print('text:', words)
print()  # blank line for readability

# Gerunds
gerunds_re = r'(\w{2,}ing)'  # Another option is (?:The|the|a|an|A|An)\s(\w{2,}ing)
print('regex for gerunds:', gerunds_re)
result_gerund = re.findall(gerunds_re, words, re.I)  # Using re.I to ignorecase
print('re.findall():', result_gerund)
print('Number of gerunds:', len(result_gerund))
print()

# Agent Nouns
agent_re = r'(\w{2,}(?:or|er))\b'
print('regex for agent nouns:', agent_re)
result_agent = re.findall(agent_re, words, re.I)
print('re.findall():', result_agent)
print('Number of agent nouns:', len(result_agent))
print()

# Recipient Nouns
recipient_re = r'\w{3,}ee\b'
print('regex for recipient nouns:', recipient_re)
result_recipient = re.findall(recipient_re, words, re.I)
print('re.findall():', result_recipient)
print('Number of recipient nouns:', len(result_recipient))
print()

# Other Nominalized verbs formed with suffixes
other_re = r'(\w{2,}(?:tion|sion|ment|ence|ance)s?)\b'
print('regex other nominalized verbs formed with suffixes:', other_re)
result_other = re.findall(other_re, words, re.I)
print('re.findall():', result_other)
print('Number of other nominalized verbs formed with suffixes:', len(result_other))  # noqa: E501
print()

# Zero-change nominalization
zero_re = r'\b((M|m)urder|(U|u)se|(C|c)hange)\b'  # Just using the three examples we are provided
print('regex for zero-change:', zero_re)
result_zero = re.findall(zero_re, words, re.I)
print('re.findall():', result_zero)
print('Number of zero-change nominalizations:', len(result_zero))
print()

# Conclusion
total = result_gerund + result_agent + result_recipient + result_other + result_zero  # noqa: E501
print('Total number of nominalizations:', len(total))
