#!/usr/bin/env', 'python3
#', '-*-', 'coding:', 'utf-8', '-*-
"""
Assignment: Create a single program that:

1. Creates one word list for each of the registers in the Mini-CORE corpus.
Exclude all function words from your frequency lists. You can use the list on
the following webpage (see the complete list at the bottom of the page): 
http://myweb.tiscali.co.uk/wordscape/museum/funcword.html. 

2. Writes each of 
these word lists to its own file, ordered according to frequency 
(highest frequency words first).

3. In 1-2 paragraphs, describe any differences you see between the lists. 
What can you learn about these registers based on these differences?
 

# POINTERS

-Use list comprehension for removing function words (make sure the function_words object is a set() for faster performance):

words = [word for word in words if word not in function_words]
-To sort a dictionary (like your frequency distributions), use sorted() with a lambda function to sort dict.items().




Created', 'on', 'Wed', 'Feb', '14', '15:00:50', '2018

@author:', 'briancroxall
"""
import nltk
from nltk.probability import FreqDist
from glob import glob
import re


def clean(words):
    # Function to clean out the metadata, tags, and headers
    clean_re = r'<p>(.*)'  # noqa: E501 regex to find text within <p> tags only. Didn't take header text
    clean_text = re.findall(clean_re, words)  # noqa: E501 use findall to get text and assign it
    join_clean = ' '.join(clean_text)  # noqa: E501 what findall returns is a list of strings, so those strings need to be joined again
    return join_clean


def extract_genre(filename):
    # Function to extract genre from file name
    short_file = filename.split('/').pop()  # noqa: E501 splits the file name on slashes and keeps the last part and saves it to the variable
    prefix = short_file.split('+')  # noqa: E501 splits the file on the pluses and saves the list to the variable
    register = prefix[1]  # noqa: E501 takes the 1th index of the list, which is what I needed, and saves it to the variable
    return register  # returns the genre


"""
    
for each in glob('Mini-CORE/*.txt'):   # for loop to iterate over corpus
    with open(each, 'r') as read_file:  # noqa: E501 read each file in the for-loop to prevent doing it multiple times in each different feature function
        text = read_file.read().lower()  # noqa: E501 opens the file, reads the file, and lowercases the file and saves it to the variable
        cleaned_text = clean(text)  # process text through clean function
        tokens = nltk.word_tokenize(cleaned_text)  # noqa: E501 tokenizes the file that had been saved to the variable
        tokens_fd = FreqDist(tokens)  # noqa: E501 takes the frequency distribution of the tokens
"""

function_words = ['A', 'ABOUT', 'ABOVE', 'AFTER', 'AGAIN', 'AGO ALL', 'ALMOST', 
                  'ALONG', 'ALREADY', 'ALSO', 'ALTHOUGH', 'ALWAYS', 'AM', 
                  'AMONG', 'AN', 'AND', 'ANOTHER', 'ANY', 'ANYBODY', 
                  'ANYTHING', 'ANYWHERE', 'ARE', 'AREN\'T', 'AROUND', 'AS', 
                  'AT', 'BACK', 'ELSE', 'BE', 'BEEN', 'BEFORE', 'BEING', 
                  'BELOW', 'BENEATH', 'BESIDE', 'BETWEEN', 'BEYOND', 
                  'BILLION', 'BILLIONTH', 'BOTH', 'EACH', 'BUT', 'BY', 'CAN', 
                  'CAN\'T', 'COULD', 'COULDN\'T', 'DID', 'DIDN\'T', 'DO', 
                  'DOES', 'DOESN\'T', 'DOING', 'DONE', 'DON\'T', 'DOWN', 
                  'DURING', 'EIGHT', 'EIGHTEEN', 'EIGHTEENTH', 'EIGHTH', 
                  'EIGHTIETH', 'EIGHTY', 'EITHER', 'ELEVEN', 'ELEVENTH', 
                  'ENOUGH', 'EVEN', 'EVER', 'EVERY', 'EVERYBODY', 'EVERYONE', 
                  'EVERYTHING', 'EVERYWHERE', 'EXCEPT', 'FAR', 'FEW', 
                  'FEWER', 'FIFTEEN', 'FIFTEENTH', 'FIFTH', 'FIFTIETH', 
                  'FIFTY', 'FIRST', 'FIVE', 'FOR', 'FORTIETH', 'FORTY', 
                  'FOUR', 'FOURTEEN', 'FOURTEENTH', 'FOURTH', 'HUNDRED', 
                  'FROM', 'GET', 'GETS', 'GETTING', 'GOT', 'HAD', 'HADN\'T', 
                  'HAS', 'HASN\'T', 'HAVE', 'HAVEN\'T', 'HAVING', 'HE', 
                  'HE\'D', 'HE\'LL', 'HENCE', 'HER', 'HERE', 'HERS', 
                  'HERSELF', 'HE\'S', 'HIM', 'HIMSELF', 'HIS', 'HITHER', 
                  'HOW', 'HOWEVER', 'NEAR', 'HUNDREDTH', 'I', 'I\'D', 'IF', 
                  'I\'LL', 'I\'M', 'IN', 'INTO', 'IS', 'I\'VE', 'ISN\'T', 
                  'IT', 'ITS', 'IT\'S', 'ITSELF', 'JUST', 'LAST', 'LESS', 
                  'MANY', 'ME', 'MAY', 'MIGHT', 'MILLION', 'MILLIONTH', 
                  'MINE', 'MORE', 'MOST', 'MUCH', 'MUST', 'MUSTN\'T', 'MY', 
                  'MYSELF', 'NEAR', 'NEARBY', 'NEARLY', 'NEITHER', 'NEVER', 
                  'NEXT', 'NINE', 'NINETEEN', 'NINETEENTH', 'NINETIETH', 
                  'NINETY', 'NINTH', 'NO', 'NOBODY', 'NONE', 'NOONE', 
                  'NOTHING', 'NOR', 'NOT', 'NOW', 'NOWHERE', 'OF', 'OFF', 
                  'OFTEN', 'ON', 'OR', 'ONCE', 'ONE', 'ONLY', 'OTHER', 
                  'OTHERS', 'OUGHT', 'OUGHTN\'T', 'OUR', 'OURS', 'OURSELVES',
                  'OUT', 'OVER', 'QUITE', 'RATHER', 'ROUND', 'SECOND',
                  'SEVEN', 'SEVENTEEN', 'SEVENTEENTH', 'SEVENTH', 'SEVENTIETH',
                  'SEVENTY', 'SHALL', 'SHAN\'T', 'SHE\'D', 'SHE', 'SHE\'LL',
                  'SHE\'S', 'SHOULD', 'SHOULDN\'T', 'SINCE', 'SIX', 'SIXTEEN',
                  'SIXTEENTH', 'SIXTH', 'SIXTIETH', 'SIXTY', 'SO', 'SOME',
                  'SOMEBODY', 'SOMEONE', 'SOMETHING', 'SOMETIMES', 'SOMEWHERE',
                  'SOON', 'STILL', 'SUCH', 'TEN', 'TENTH', 'THAN', 'THAT',
                  'THAT', 'THAT\'S', 'THE', 'THEIR', 'THEIRS', 'THEM',
                  'THEMSELVES', 'THESE', 'THEN', 'THENCE', 'THERE',
                  'THEREFORE', 'THEY', 'THEY\'D', 'THEY\'LL', 'THEY\'RE',
                  'THIRD', 'THIRTEEN', 'THIRTEENTH', 'THIRTIETH', 'THIRTY',
                  'THIS', 'THITHER', 'THOSE', 'THOUGH', 'THOUSAND',
                  'THOUSANDTH', 'THREE', 'THRICE', 'THROUGH', 'THUS', 'TILL',
                  'TO', 'TOWARDS', 'TODAY', 'TOMORROW', 'TOO', 'TWELFTH',
                  'TWELVE', 'TWENTIETH', 'TWENTY', 'TWICE', 'TWO', 'UNDER',
                  'UNDERNEATH', 'UNLESS', 'UNTIL', 'UP', 'US', 'VERY', 'WHEN',
                  'WAS', 'WASN\'T', 'WE', 'WE\'D', 'WE\'LL', 'WERE', 'WE\'RE',
                  'WEREN\'T', 'WE\'VE', 'WHAT', 'WHENCE', 'WHERE', 'WHEREAS',
                  'WHICH', 'WHILE', 'WHITHER', 'WHO', 'WHOM', 'WHOSE', 'WHY',
                  'WILL', 'WITH', 'WITHIN', 'WITHOUT', 'WON\'T', 'WOULD',
                  'WOULDN\'T', 'YES', 'YESTERDAY', 'YET', 'YOU', 'YOUR',
                  'YOU\'D', 'YOU\'LL', 'YOU\'RE', 'YOURS', 'YOURSELF',
                  'YOURSELVES', 'YOU\'VE']
stop_words = set([word.lower() for word in function_words])

with open('IN.txt', 'w') as my_file:
    for each in glob('Mini-CORE/1+IN*.txt'):
        with open(each, 'r') as read_file:
            words = []
            text = read_file.read().lower()
            cleaned_text = clean(text)
            tokens = nltk.word_tokenize(cleaned_text)
            tokens_fd = FreqDist(tokens)
            for token, freq in tokens_fd:
                if token not in stop_words:
                    print(token, freq, sep="\n", my=my_file)
                else:
                    continue