# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:47:43 2014

@author: hannah
"""

# you do not have to use these particular modules, but they may help
from random import randint, choice
import math
import Image



def build_random_function(min_depth, max_depth):

    our_functions=['prod','X','Y', 'cos_pi', 'sin_pi','squared','cubed' ]#list of function names
    n=randint(0,6)#giving values to indecies of our_functions
    """ Takes two inputs, min_depth(minimum amount of nesting) and max_depth(
    specidfies maximum amount of nesting. Should use recurssion
    
        Pulls from 5 different functions, need input between 1 and -1, output 1 and -1
        add two more of your own functions that do said above""" 
    if max_depth==1 :
        return choice(['x','y'])#returning x or y
    if n >2: #causing "break" of the function list. All abo
        return [our_functions[n], build_random_function(min_depth-1, max_depth-1)]#the recursion that branches to base case, eventually, one arguments go in
    else:   
        return [our_functions[n], build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]#two arguments created, same idea about branching recursion from before
print build_random_function(0, 2)        

def evaluate_random_function(f,x,y):
    """here this function will take in a list (created from the build random function), and two inputs between -1 and 1. This 
    returns a number, becuse the strings are actually evaluated. This then creates the answer to the recursive formula. This
    solves the different cases of the formula depending on x and y. """
    if f[0]=='x':#base case x
        return x
    if f[0]=='y':#base case y
        return y
    if f[0]=='prod':
        return evaluate_random_function(f[1], x,y)*evaluate_random_function(f[2], x,y)#multiplying second and third indice (which is the argumenst of function (first indice)(originally two arguments))
    if f[0]=='X':
        return evaluate_random_function(f[1], x,y)#chooses first argument(two arguments originally)
    if f[0]=='Y':
        return evaluate_random_function(f[2], x,y)#chooses second argument (two arguments orginally)
    if f[0]=='cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1], x,y)) #evaluates cos of one argument (only one argument)
    if f[0]=='sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1], x,y)) #evaluates sin of one argument (only one argument)
    if f[0]=='squared':
        return (evaluate_random_function(f[1], x,y))**2 #squares first "argument"
    if f[0]=='cubed':
        return (evaluate_random_function(f[1], x,y))**3 #cubes first "argument"


    
#desktop pixel size

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        It takes a number in one range and gives it back as number in a different range. "It moves pixels
        from big to small".
    """
    Crazy_math=float((val-input_interval_start))
    Difference_of_input=float(input_interval_end-input_interval_start)
    fraction=float(Crazy_math/(Difference_of_input))
    Difference_of_output=(output_interval_end-output_interval_start)
    Thing_to_add_to_output_interval_start=Difference_of_output*fraction
    answer=Thing_to_add_to_output_interval_start+output_interval_start
    return answer
    
def pretty_little_masterpiece(filename):
    """create the image of the pretty pictures. Take the RGB functions and change the pixelation. This then fills the empty
    image that is created."""
    function_red=build_random_function(0,6)
    function_green=build_random_function(0,7)
    function_blue=build_random_function(0,5)
    im=Image.new("RGB",(1600,900)) 
    pixels=im.load()
    for x in range(0,1600):# this loop looks at the color of x value...
        for y in range (0,900):#for every y value (nested loop)
            rawx=remap_interval(x, 0, 1600, -1,1)#changing range analysis
            rawy=remap_interval(y, 0, 900, -1,1)
            green_image=remap_interval(evaluate_random_function(function_green, rawx, rawy), -1,1, 0,225)#green 
            red_image=remap_interval(evaluate_random_function(function_red, rawx, rawy), -1, 1, 0,225)
            blue_image=remap_interval(evaluate_random_function(function_blue, rawx, rawy),-1, 1, 0,225)
            pixels[x,y]=(int(red_image), int(green_image), int(blue_image))
            
    im.save(filename)
            
