#  -*- coding: utf8 -*-
# Exercise 19: Functions and Variables

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 19: Functions and Variables"

print
print

# Variables in functions are not connected to variables in the script.
# Function variables are disconnected from script variables.
# They have a different scope?

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "    = = = = = = = = = = = "
    print "    Aw yis, .ch 4eva - u have %d cheeses!" % cheese_count
    print "    You have %d boxes of crackers!" % boxes_of_crackers
    print "    Mate that's enough for a tops picnic!"
    print "    Grab a blankets let's go!"
    print "    = = == = == = = == = == ="
    print
    
print "Ok we gonna give the numbers directly to the function,"
print "by typing cheese_and_crackers(11, 111) : "
cheese_and_crackers(11, 111)

print "OR, we can declare some variables in the script, and then"
print "call the definition using these variables:"
amount_of_cheese = 20
amount_of_crackers = 220
cheese_count = 555

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "But the fun continues - we can do maths inside the fn call too!"
print "For instance, cheese_and_crackers(10 + 20, 300 + 33)"
cheese_and_crackers(10 + 20, 300 + 33)

print "Yes, you can mix it up, check it out like this:"
print "cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 220)"
cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers + 220)


print
print

print "=================================================="