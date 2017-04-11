#  -*- coding: utf8 -*-
# Exercise 21: Returning values from a Function

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 21: Returning values from a Function"

print
print

# In the following, we take a result or calculation from inside the 
# function, and make it returnable.  
# The value then moves from inside the scope of the function, to the 
# scope of the rest of the script.

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    

print "Let's do some maths, only using functions!"

# Here, we declare a variable called 'age', and fetch its value from
# the returned result of the function add().

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Shall we continue?"
raw_input()

print "Age: %d, Height %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print
print

# A puzzle for extra credit, type it in anyway
# The point is that the variables age, height etc have values from the 
# above bit of the script.  We then call the fns again, using 
# the variables as aliases for actual numeric values.

# For instance, iq is now equal to 50.
# So divide(iq, 2) is the same as divide(50, 2), which is 25
# Then, multiply(weight, divide(iq, 2)) is multiply(weight, 25)
# Which is multiply(180, 25), which is 4500.
# And so on :)
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# The equivalent in normal maths notation would be:
# age + (height - (weight.(iq/2)))

print "That becomes: ", what, "Can you do it by hand?"


print
print

print "=================================================="