#  -*- coding: utf8 -*-
# Exercise 20: Functions and Files

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 20: Functions and Files"

print
print

# This script gets the read point from user input, and then prints
# three consecutive lines from the file, starting at the read point.

from sys import argv

script, input_file = argv

current_file = open(input_file)
 
# -- print_all()
# reads a user-specified file, and prints it to the screen.
def print_all(f):
    print f.read()

# -- rewind()
# places the read head at a user-defined point.
# gets its input from start_point, down below.    
def rewind(f, read_head):
    f.seek(read_head)

# -- print_a_line()
# prints out the line number and the corresponding line's text, and a CR
def print_a_line(f, line_count):
    print line_count, f.readline(),
    

# Hello world
print "First let's print the whole file.\n"
print_all(current_file)
print


# ----
# This section asks the user to define the position of the read head,
# and then passes that value into the rewind fn.
start_point = int(raw_input("What position in the file shall we start at? "))
rewind(current_file, start_point)

# ---
# This section takes the above user-defined start_point, and uses it to 
# set the value of current_line, which is then passed to print_a_line().
# current_line is then incremented twice more, to print out three lies
# in total.

print
print "OK we gonna print three lines checkit:"

current_line = start_point
print_a_line(current_file, current_line)

current_line += 1
print_a_line(current_file, current_line)

current_line += 1
print_a_line(current_file, current_line)

current_file.close()

print "=================================================="