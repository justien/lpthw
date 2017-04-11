#  -*- coding: utf8 -*-
# Exercise 32: Custom Loop

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 32: Custom Loop"

print
print

start = int(raw_input("Please supply a start value: "))
stop = int(raw_input("Please supply a stop value: "))
step = int(raw_input("Please supply the size of the step: "))

print "Let's increment from %s in steps %s high, until we reach %s." % (start, step, stop)
print

value = start # I'm reassigning this coz I might want to use start later on.

print

# this loop doesn't execute because script thinks that value < stop is FALSE.
# why???? Because originally I had the raw_input, instead of int(raw_input)
# Now when I convert the raw_input to an int, it works.

while (value < stop):
    print "Value is: %d" % value
    value = value + step

print
print

print "======================================================================="	