# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:53:18 2014

@author: madeleine
"""

from sets import Set


B = ['break','shattered','broken','breaks','shatter','fracture','fractured','splinter','splintered','breaking','shattering','fracturing','splintering','fragment','rend','crack','cracked','cracking','cracks','schism','rift']
P = ['Him','Her','He','She','We','Ours','Our','They','I','Me','Mine','Theirs','Yours','Who','Whoever','Everybody']    

    
    
def getSentences(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences

def make_list(book):
    count = 0
    for sentence in getSentences(book.lower()):
        for b in B:
            word1 = b.lower()
            for p in P:
                word2 = p.lower()
                if word1 in sentence and word2 in sentence and sentence not in lst:
                    count = count + 1
    return count
    

list_of_books = ["book1.txt", "book2.txt", "book3.txt"]

final = {}

for book_name in list_of_books:
    f = open(book_name,'rb')
    book  = f.read()
    final[book_name] = make_list(book)
    f.close()
    








