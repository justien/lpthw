#  -*- coding: utf8 -*-
# Exercise 17: More Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 17: More Files"

print
print

# Comment comment

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "This script will copy content from %s to %s ... " % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
input_file_contents = open(from_file).read()


print
print "The input file %s is %d bytes long." % (from_file, len(input_file_contents))
print "Does the output file exist? \n\t%r" % exists(to_file)
print
print "Ready: hit RETURN to continue, CTRL-C to abort."
raw_input()

# Note that if to_file does not exist, python will CREATE it at this stage.
# This works for pdf and png as well as for txt. 
print
print "Writing the contents of %s to %s now." % (from_file, to_file)
out_file_obj = open(to_file, 'w')
out_file_obj.write(input_file_contents)

print
print "The target %s now reads:\n" % to_file
out_file_obj.close()
#to_file_contents = open(to_file)
print open(to_file).read() 

print 

out_file_obj.close()

input_file_obj.close()

print
print

print "=================================================="