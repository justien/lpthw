#  -*- coding: utf8 -*-
# Exercise 20: Functions and Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 20: Functions and Files"

print
print

# This script gets the read point from user input, puts the point at
# the beginning of that line, and then prints three consecutive lines
# from the file, starting at the read point.

# OK, no with what we have so far, we can't do this.
# This is because a. the print_a_line fn is entirely relative to start_point
#                 b. readline() doesn't move backwards

# But what we can do is emit the next three whole lines which follow
# the start_point.

from sys import argv

script, input_file = argv

current_file = open(input_file)

# Places the read head at start_point, then goes to start of next line.  
def rewind(f, read_head):
    f.seek(read_head)
    f.readline()
    
def print_a_line(f):
    print f.readline(),


print "Working on file %s: " % input_file
start_point = int(raw_input("Please enter a start position: "))
rewind(current_file, start_point)



# ---
# This section takes the above user-defined start_point, and uses it to 
# set the value of current_line, which is then passed to print_a_line().
# current_line is then incremented twice more, to print out three lies
# in total.

print
print "OK we gonna print the next three whole lines checkit:"

current_line = start_point
print_a_line(current_file)

current_line += 1
print_a_line(current_file)

current_line += 1
print_a_line(current_file)

current_file.close()

print "=================================================="