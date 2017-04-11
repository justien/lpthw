#  -*- coding: utf8 -*-
# Exercise 12: Prompting People

print "=================================================="
print "Exercise 12: Prompting People"

print
print

name = raw_input("What is your name? ")
age = raw_input("How old are you, \nin %s years? " % "cat")
height = raw_input("How tall are you, in centimeters? ")
weight = raw_input("How much do you weigh in kilograms? ")

print "So, %s - you're %s cat years old, %s centimetres tall, and %s in kilos." % (
    name, age, height, weight)

print
print

print "\t Zed Shaw wants us to memorise the following:"
print "\t\t %r is for debugging"
print "\t\t\t it is the raw representation (whatever that means)"
print " \t\t %s is for display"

print

print "the original format of this exercise is as follows."
print "note that it uses %r, and not %s"

print

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print " So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print

print "=================================================="
