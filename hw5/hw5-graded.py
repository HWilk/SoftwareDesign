# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:53:18 2014

@author: madeleine
"""
B = ['break','shattered','broken','breaks','shatter','fracture','fractured','splinter','splintered','breaking','shattering','fracturing','splintering','fragment','rend','crack','cracked','cracking','cracks','schism','rift']
P = ['Him','Her','He','She','We','Ours','Our','They','I','Me','Mine','Theirs','Yours','Who','Whoever','Everybody']    

f = open('HeartofDarkness.txt','rb')
BookH  = f.read()
f.close()
from sets import Set

def getSentences(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences
li = []

for sentence in getSentences(BookH.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                li.append(sentence)

#print Set(li)
print len(Set(li))

f = open('Metamorphosis.txt','rb')
BookM  = f.read()
f.close()

def getSentences2(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences

la = []

for sentence in getSentences2(BookM.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                la.append(sentence)

#print Set(la)
print len(Set(la))

f = open('OnceaGreech.txt','rb')
BookOG  = f.read()
f.close()

def getSentences3(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences

lp = []

for sentence in getSentences3(BookOG.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                lp.append(sentence)

#print Set(lp)
print len(Set(lp))

f = open('LesMiserables.txt','rb')
BookLM  = f.read()
f.close()


def getSentences4(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences

lw = []

for sentence in getSentences4(BookLM.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                lw.append(sentence)

#print Set(lw)
print len(Set(lw))

f = open('WarandPeace.txt','rb')
BookWP  = f.read()
f.close()


def getSentences5(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences


lh = []

for sentence in getSentences5(BookWP.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                lh.append(sentence)

#print Set(lh)
print len(Set(lh))

f = open('siddhartha.txt','rb')
BookS  = f.read()
f.close()


def getSentences6(x):
    sentences = []
    while len(x) > 0:
        index = x.find('.')+1
        sentences.append(x[:index])
        x = x[index+1:]
    return sentences

lq = []

for sentence in getSentences(BookS.lower()):
    for b in B:
        word1 = b.lower()
        for p in P:
            word2 = p.lower()
            if word1 in sentence and word2 in sentence:
                lq.append(sentence)

#print Set(lq)
print len(Set(lq))

Final = {'Heart of Darkness':len(Set(li)),'Metamorphosis':len(Set(la)),'Once a Greech':len(Set(lp)),'Les Miserables':len(Set(lw)),'War and Peace':len(Set(lh)),'Siddhartha':len(Set(lq))}

print Final



