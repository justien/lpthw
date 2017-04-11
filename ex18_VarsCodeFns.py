#  -*- coding: utf8 -*-
# Exercise 18: Variables, Code, Functions

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 18: Variables, Code, Functions"

print
print

# !!! --- Functions --- !!!
#
# Functions do three things:
#	1. They name pieces of code the way variables name strings and numbers
#	2. They take arguments the way your scripts take argv
#	3. 1 + 2 = mini-scripts  
# 
#          ^------- SO MUCH WIN

# this one is like your scripts with argv
#
# Zed says this way of unpacking arguments is skippable in python.
# He says: this tells Python to take all arguments to the function
# and then put them in args as a list.
#
# When would you need to do this?
# 1. When list elements need to be combined a special way?
# 2. Maybe a list brings special properties which could be useful later,
#    like perhaps ... being able to count the elements, or get stats 
#    about the elements, or ask for the nth list item?


def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
    # args ... can it be defined outside the function?
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# this takes just one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments at all. none.
def print_none():
    print "I got nuthin."
    
print_two("Zed","Shaw")
print_two_again("Tzed","Zhaw")
print_one("First!")
print_none()   

print
print

print "=================================================="