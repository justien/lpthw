#  -*- coding: utf8 -*-
# Exercise 33: While Loops

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 33: While Loops"

print
print

# While loops can go on forever, like a droning guest at a dinner party.
# How to avoid:
#    Use them sparingly
#    Check that the bool will test false at some point
#    Chuck in a debugger print to keep an eye on things

def stepping(begin, limit, step):
    i = int(begin)
    stop = int(limit)
    step = int(step)
    numbers = []
    
    while i < stop:
        print "This loop starts at %d" % i
        numbers.append(i)
        
        i += step
        
        print "See the list: ", numbers
        print "This loop ends with %d" % i
        print
        
    print "The list, finally: "
    
    for num in numbers:
        print num

print "Hello let us make a list"
print "We need three parameters."
a = raw_input("Please supply a starting value: ")
b = raw_input("Please supply the upper boundary value: ")
c = raw_input("Please choose the size of the steps: ")
stepping(a, b, c)

print
print

print "======================================================================="