#  -*- coding: utf8 -*-
# Exercise 11: Asking Questions

print "=================================================="
print "Exercise 11: Asking Questions"

print
print

# With this formulation, I can combine the string name with the question 
# and the raw_input all at once.

name = raw_input("What is your name? ")
print "Hello, %s." % name

# Wrapping raw_input() in int() converts the raw input into an integer
print "How old are you, in years?",
age = int(raw_input())

print "How tall are you, in centimetres?",
height = int(raw_input())

print "How much do you weigh, in kilos?",
weight = int(raw_input())

print

print "So %s, you're %r years old, %r centimetres tall, and you weigh %r kilos." %(
    name, age, height, weight)



print
print

print "=================================================="
