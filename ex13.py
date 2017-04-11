#  -*- coding: utf8 -*-
# Exercise 13: Parameters, Unpacking, Variables

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 13: Parameters, Unpacking, Variables"

print
print

# --Importing a function from a library
#   Here we import a particular function from a library.
#   This has the effect of using only a small amount of memory, 
#   rather than blowing it out by importing everything *all* the functions.
#   It also lets future maintainers know what's being used.

# --argv - what does it mean?
#   Below, the module called 'argument vector' is imported from sys.
#   This vector holds the values of the arguments that are passed
#   to the script whilst running it.

# --my questions
#   1. This is not the same as raw_input() ... somehow ... or %s
#      where you have to put the little dictionary of string names
#      at the end of the print command
#      eg print "Hello %s and %s!" % (player1, player2) 
#   2. It tells python to give me the command line arguments that
#      the person typed in ... interesting - so the command line arguments
#      are stored by python somewhere and then used.  
#      Where are they stored, and when are they replaced?
#      How is cleanup of these variables handled?


from sys import argv

script, first, second, third = argv

print "The script is called:", script
print
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print

choice = raw_input("Choose first, second or third: ")

print
print "The %s variable's value is " % choice
print 'choice' + choice

print
print

print "=================================================="
