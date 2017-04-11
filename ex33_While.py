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

i = 0
numbers = []

while i < 6:
    print "At the top of the loop, i is %d" % i
    numbers.append(i)
    
    i += 1
    
    print "Numbers now: ", numbers
    print "At the bottom of the loop, i is %d" % i
    print
    
print "The numbers: "

for num in numbers:
    print num


print
print

print "======================================================================="