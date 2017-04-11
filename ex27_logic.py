#  -*- coding: utf8 -*-
# Exercise 27: Logic Tables

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 27 Logic Tables"

print
print

# The Nine Logical Operators in Python
#
# ==	and		True
# !=	or		False
# >=	not	
# >=

# This script creates tables showing basic logic, using a recursive loop.


def create_table_top_with(operator):
    line = "--------------"
    row1 = "    x   y  |  %s" % operator
    row2 = "   %s" % line
    tabletop = row1 + '\n' + row2
    return tabletop


# nested loops to print the binary table
# WOAH FUCK I DID A NESTED LOOP I FEEL PRETTY RAD!!!!
def fill_table_with_logic(operator):
	x = 0
	y = 0
	eval = "print x " + operator + " y"
	while (x < 2):
		while (y < 2):
			print "   ", x, " ", y, " | ",
			exec(eval)
			y = y + 1
		y = 0
		x = x + 1
        
    
# I'd like to avoid typing print create_table_top_with(operator) each time.
# But I can't figure out how to pass this to python without it being a 
# string rather than a set of commands.
# maybe this is where exec(string) comes in handy?
# OMG IT WORKS THIS IS VERY EXCITING!!!!

print_tabletop = 'print create_table_top_with(operator)'
titlebar = "\n\n====---------------------------------=="

# operator = 'not'
# print titlebar, "\n    %s" % operator
# print " NOT\tInverts the truth condition"
# exec(print_tabletop)
# fill_table_with_logic(operator)
 
operator = 'or'
print titlebar, "\n    %s" % operator
print "    True if at least one element is true\n"
exec(print_tabletop)
fill_table_with_logic(operator)


# operator = 'NOR'
# print titlebar, "\n    %s" % operator
# print "    True when both elements are false\n"
# exec(print_tabletop)
# fil_table_with_logic(operator)
 
operator = 'and'
print titlebar, "\n    %s" % operator
print "    True when both elements are true\n"
exec(print_tabletop)
fill_table_with_logic(operator)


# operator = "NAND"
# print titlebar, "\n    %s" % operator
# print "    True when one or both elements are false\n"
# exec(print_tabletop)
# fill_table_with_logic(operator)


operator = "=="
print titlebar, "\n    %s" % operator
print "    True when the elements are equal to each other"
exec(print_tabletop)
fill_table_with_logic(operator)


operator = "!="
print titlebar, "\n    %s" % operator
print "    True when the elements differ from each other"
operator = "!="
exec(print_tabletop)
fill_table_with_logic(operator)


operator = ">="
print titlebar, "\n    %s" % operator
print "    True when left is greater than or equal to right"
exec(print_tabletop)
fill_table_with_logic(operator)


operator = "<="
print titlebar, "\n    %s" % operator
print "    True when left is less than or equal to right"
exec(print_tabletop)
fill_table_with_logic(operator)


print
print

print "======================================================================="