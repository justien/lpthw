#  -*- coding: utf8 -*-
# Exercise nn: Asking Questions

print "=================================================="
print "Exercise 11: Asking Questions"

print
print

# Comment comment

name = raw_input("Hi there! What is your name? ")
print "Hello, %s." % name

print "How old are you, in years?",
age = int(raw_input("How old are you in years?"))

print "How tall are you?",
height = raw_input()

print "How much do you weigh, in kilos?",
weight = int(raw_input())

print "So %s, you're %r years old, %rcms tall, and weigh %rkgs." % (
    name, age, height, weight)


print
print

print "=================================================="
