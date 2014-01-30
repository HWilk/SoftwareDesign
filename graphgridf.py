# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:47:57 2014

@author: Hannah Wilk
"""
def do_twice(f):
    f()
    f()
    
def do_four(f):
    do_twice(f)
    do_twice(f)
        
def print_beam() :
    print '+','-','-','-','-','+','-','-','-','-','+'
    
def print_post():
    print '|        ',
y

def print_beams():
    print_beam()
    
    
def print_posts():
    do_twice(print_post)
    print '|'
    
def print_row():
    print_beams()
    do_four(print_posts)
    
def print_grid():
    do_twice(print_row)
    print_beams()
    
print_grid()