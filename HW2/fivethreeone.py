# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:19:54 2014

@author: Hannah Wilk
"""

def check_fermat(a,b,c,n):
    if n>2:
        
        if a**n+b**n == c**n:
       
           print'Holy Smokes, Fermat was wrong'
        else: print 'No, that was wrong'
        
