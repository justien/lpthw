#  -*- coding: utf8 -*-
# Exercise 20: Functions and Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 20: Functions and Files"

print
print

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file.\n"
print_all(current_file)

# This section sets the read point at the beginning of the file.
# If this is left unset, readline() returns nothing, but doesn't error.
print "Now let's rewind to the start of the file, kind of like a tape."
rewind(current_file)

print "OK we gonna print three lines checkit:"


# Pay Attention!!
# As is, this script doesn't relate current_line to the actual line being read.
# Instead we're seeing the special case where the first line = line number one,
# but this is only a coincidence.

# This section increments current_line twice.  It's really a hard-coded variable
# for when we print out the first three lines.

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print
print

print "=================================================="