#  -*- coding: utf8 -*-
# Exercise 15: Reading Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 15: Reading Files"

print
print

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print

print "\nPlease enter the filename again, including the extension:"
file_again = raw_input("---> ")

txt_again = open(file_again)

#txt_again = open(raw_input("---> "))

print txt_again.read()



""""
# Go fetch the library that tells me how to accept input from the
# command line when the script is run.
from sys import argv

# When the arguments come in from the command line, as the script is called, 
# call the first arg "script" and the second arg "filename".
script, filename = argv

# Create a variable called "txt".  This variable is composed using 
# the argument "filename", first introduced above from the command 
# line.
# This variable is formatted so that it calls the method open().
# In fact, what we have here is the creation of a FILE OBJECT
txt = open(filename)

# Now that we have the filename, we print out a statement that
# confirms the filename.  We then print out the contents of the  
# file, using the open() and read() methods to fetch the file
# contents into memory.
print "Here's your file %r:" % filename
print txt.read()

# I'm going to say a few more words on this.  We're taking 
# open(filename) and giving it a command - the command of read()
# But as yet, we have no idea in which security context we open 
# the file, nor in which context we read the file.  It just works.

# EXTRA FUN!  Try saving and then opening a word or pdf file.
# I got my word doc to make python beep ;)


# Now the script asks us to enter in the filename one more time.
# The input is collected via the raw_input() method, with a nice
# angle-bracket prompt for the user to feel hack.
# This user input becomes the value of the string "file_again"
print "Type the filename again:"
file_again = raw_input(">")

# The script uses "file_again" to prepare a shortcut - it calls the 
# the open() method.  Open what? Open it pre-populated'd with the input 
# collected just above from the hack prompt!
txt_again = open(file_again)

print

# The script, using the finest of hand-labelled strings, finds out
# the name of the file to be opened, reads it, and then gets 
# their good friend 'print' to do her thang.
print txt_again.read()

# now we tidy up the open files, and close the drawers
txt.close()
txt_again.close()
"""


print "=================================================="
