# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:19:54 2014

@author: Hananh Wilk
"""

def check_fermat(x,y,z,w):   
   if w>2:
       if x**w+y**w == z**w:
           print'Holy Smokes, Fermat was wrong'
       else: print 'No, that was wrong'
         

def run_fermat():
    a=raw_input('What is a value of A?')
    int(a)
    b=raw_input('What is a value of B?')
    int(b)
    c=raw_input('What is a value of C?')
    int(c)
    n=raw_input('What is a value of n?')        
    int(n)
    x=int(a) 
    y=int(b)
    z=int(c)
    w= int(n)
    check_fermat(x,y,z,w)
           
#Thankyou James Jang&Nick Francisci
