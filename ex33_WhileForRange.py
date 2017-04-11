#  -*- coding: utf8 -*-
# Exercise 33: While Loops

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 33: While Loops"

print

# While loops can go on forever, like a droning guest at a dinner party.
# How to avoid:
#    Use them sparingly
#    Check that the bool will test false at some point
#    Chuck in a debugger print to keep an eye on things

def stepping(begin, limit, step):
    start = int(begin)
    stop = int(limit)
    step = int(step)
    numbers = []
    
    for i in range(start, stop, step):
        print "This loop starts at %d" % i
        numbers.append(i)

# Any calculation on i within the loop will have NO EFFECT on the movement of 
# i through the sequence defined by range().
        i = 769
# Here, i is set to a silly value.

# When the loop returns to the top, i's value changes again, this time to 
# be the next set in the sequence defined by range().

# So python has its own secret counter, defining the current position in the 
# range, which is independant of the value of i.
        
        print "See the list: ", numbers
        print "This loop ends with %d" % i
        print
        
    print "The list, finally: "
    
    for num in numbers:
        print num

print "Hello let us make a list, we need three parameters."
a = raw_input("Please supply a starting value: ")
b = raw_input("Please supply the upper boundary value: ")
c = raw_input("Please choose the size of the steps: ")
stepping(a, b, c)

print

print "======================================================================="