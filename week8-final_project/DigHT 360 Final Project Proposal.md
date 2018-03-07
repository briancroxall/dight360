# DigHT 360 Final Project Proposal

## What do you want to accomplish and why?
For the project, I would like to conduct some supervised machine learning on a corpus of poems by Carol Ann Duffy. In particular, I’m interested to see the degree to which her fifth volume of poems, _The World’s Wife_ (1999) differs from the previous four volumes that she published: _Standing Female Nude_ (1985), _Selling Manhattan_ (1987), _The Other Country_ (1990), and _Mean Time_ (1993). 

This idea was spurred by a letter my students and I found in [special collections](https://findingaids.library.emory.edu/documents/duffy834/series1/) at Emory University. This letter was written to editor at Anvil Books, which had published Duffy’s first four volumes and had a contract for _The World’s Wife_. In the letter, Duffy breaks the contract, citing two different reasons. One reason is that she has a daughter now and wants to make more money with the book. The other reason, she writes, is that “this book [_TWW_] is not a ‘normal’ poetry collection by me—it’s close to popular entertainment.” I’ve been working on this problem across four iterations of “Introduction to Digital Humanities,” including in BYU’s DigHT 215 course during Fall 2017. And I’m currently teaching a whole semester of DigHT 315 that focuses solely on this question. Pursuing this as a final project seems to like a good way to continue to extend what I am learning about the differences among the volumes and will give me something new to contribute to the class I’m currently teaching. I hope that this will eventually become part of a larger article.

I think that of all the homework we have done to date, the closest to this project was the machine learning. That said, I’m not sure if building a set of features so that TWW can be predicted as the origin point vis a vis the other books is quite what I want to do. What I am after is the difference / similarity among that book and its predecessors. Of course, the feature sets might be good proxies for these differences. 

N.B. I know that one of my 215 students from Fall 2017, Mike Kim, tackled this project last semester. As such, I owe him a debt for the good idea.   

N.B. I think the high school mascot idea is actually a lot more fun, but this one seems to dovetail nicely with what I’m doing in the class I’m teaching at the moment. 

## How will this help you develop the programming skills you will need in the future?
I imagine that a lot of my programming in the future will be related to one form of textual analysis or another. This will provide me with the opportunity to become better at 1) cleaning texts, 2) parsing them with NLTK, and 3) coming up with features that I can use to test for differences. 

## What data will you use?
Over the years, my students and I have built digital editions of the books by transcribing the poems. This semester, my students and I are preparing TEI editions of the books, which will provide an opportunity to double-check all of the past work. 

## What is your plan to carry out this project
### How will you get the data?
I already have the data to hand, at least in the old plain text versions. If I wanted to use the new TEI editions, those will be completed shortly. 

### How will you accomplish the programming tasks?
I anticipate doing the following:
* Parsing the XML with BeautifulSoup
* Tokenizing the texts with NLTK
* Building a number of feature sets to include the following
	* pronouns
	* parts of speech tagging
	* punctuation
	* sentiment analysis
	* using the metadata that my students and I are collecting this semester
* Building on the template of the machine learning homework

### How will you ensure accuracy?
I think that the answer to this question is carving my data into training and validation sets and then doing cross-validation to train the models.  I will try to add as many features as possible and keep doing the cross-validation until I get an acceptable level of accuracy.

If it’s a question of how I check the accuracy of the data, that is already being taken care of with the work that my students and I are doing for the class project of TEI editions. 

## 	What programming and/or python skills will you need for this project?
I think that I have acquired most of the skills that I need for the project already or, rather, that our class has covered all of the major skills. That said, I imagine I can improve in a number of these areas. I can certainly learn more about different sentiment analysis modules and the creation of machine learning feature sets. Outside of Python, I will need to learn more about the different things to take into account when cleaning a text for use in a manner like this. 
