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

"""
I've added this close as a kind of hack debugger on the 
the state of the file, maybe I can see this change in 
the text editor whilst the script waits for user input
a bit further down.
Nope that didn't work with TextWrangler, at any rate.
So there is this thing called getattribute in the pydoc,
gonna try that ... err no I am not. But I'll move this idea
to my thoughts file, no worries.
"""

print "Truncating and closing %s ... Goodbye!" % filename
target.truncate()
target.close()


print

print "Reopening %s in write mode." % filename
target = open(filename, 'w')

print

print "Please supply three lines of text: "

line1 = raw_input("\tLine 1: ")
line2 = raw_input("\tLine 2: ")
line3 = raw_input("\tLine 3: ")

"""
OK, Zed asks us to rewrite the following so that instead of six
target.write() commands, there is only one.

It turns out that the target.write() function can only take one
argument, so something like target.write(line1, line2) throws an
error.

Possible ways around this:
1. write a bunch of strings as aliases, so that what sits inside
	the target.write() is only 'one' function.  Feels ugh.
2. write a bunch of strings, then one string, which when unpacked
	is the same as six target.write() fns.  Also kind of ugh.

trying approach 1 first ...
"""
firstline = "%s\n" % line1
secondline = "%s\n" % line2
thirdline = "%s\n" % line3
allthelines = firstline + secondline + thirdline
target.write(allthelines)

print 

print "Thanks."
print "Lines now appended to %s." % filename

"""
 --- !! NOTE WELL !!--- 
the file must be closed here, otherwise open() below will only
see the truncated file, without the appended lines. 
print "Lines succesfully appended and file closed."
"""
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
