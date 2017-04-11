#  -*- coding: utf8 -*-
# Exercise 16: Reading and Writing Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 16: Reading and Writing Files"

print
print

# This script opens a specified file, wipes the contents, and
# then adds three new lines of user-supplied text to the file.
# Usage: scriptname [filename]

from sys import argv

script, filename = argv

print "This script will erase the contents of %s" % filename
print "and then let you write three new lines of text to it."
print
print "To prevent deletion of the file contents, hit ctrl-c NOW (^C)."
print "To continue with deletion, press return."

raw_input("\n--->? (return or ctrl-c)")

print 

print "Opening the file as writable now ..."
target = open(filename, 'w')

print "Truncating %s ... Goodbye!" % filename
target.truncate()

print

print "Please supply three lines of text: "

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print 

print "Thanks."
print "Lines now being appended to %s." % filename

target.write(line1)
target.write("\n")
print "."
target.write(line2)
target.write("\n")
print "."
target.write(line3)
target.write("\n")
print "."

# --- !! NOTE WELL !!--- 
# the file must be closed here, otherwise open() below will only
# see the truncated file, without the appended lines. 
print "Lines succesfully appended and file closed."
target.close()

print

print "%s is now:" % filename
currentfile = open(filename)
print currentfile.read()

print

# target.close()
print "%s now closed." % filename


print
print

print "=================================================="