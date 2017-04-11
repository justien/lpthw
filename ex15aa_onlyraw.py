#  -*- coding: utf8 -*-
# Exercise 15: Reading Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 15: Reading Files"

print
print

print "Enter the name of the file to open: "
filename = raw_input("---> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print

# now we tidy up the open files, and close the drawers
txt.close()

# ... I wonder if this means that filename has been opened twice?
# and if that is potentially a problem?

print "=================================================="
