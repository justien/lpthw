#  -*- coding: utf8 -*-
# Exercise 19a: Functions and Variables extension

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 19a: Functions and Variables extension"

print
print

# This is where I get to write my own function.
# What would be useful?
# Well let's think about my tarot card generator ... no that's too heavy.
# TBH it seems a bit weird right now since the function might as well
# be the same as a python script that gets runs a lot of ways.
# Ugh I find it hard to think of cool things that'll fit in what we already
# have and no more.

# Things to test:
# 1. Can I pass the variables from argv? Yes.
# 2. Can I write it to get the arguments from raw_input? Yes.
# 3. ... a combo of argv and raw_input? Yes.

from sys import argv

script, name = argv

def chook_shed(chook_num, yard_type):
    min_nest = chook_num * 1.3
    min_range = chook_num * 3.3
    print 
    print "OK, with %s chooks, and a %s yard, those chook'll need at least" % (chook_num, yard_type) 
    print "\t %s square metres for nesting, and" % min_nest
    print "\t %s additional square metres to move around." % min_range
    

print """
--0--O--o--O--0----0--O--o--O--0----0--O--o--O--0----0--O--o--O--0--

%s - today was a tops day!
You went to your neighbour's place and they gave you a box.
Mate, inside the box were chickens!

--0--O--o--O--0----0--O--o--O--0----0--O--o--O--0----0--O--o--O--0--
""" % name


print
print

print "It's kind of exciting."
print
print """
\t   (o>
\t\\_//)
\t\_/_)
\t  _|_
"""
print "Life is good."

print
print

print "Farmer %s - obvs you care about your new chooks." % name
chook_factor = int(raw_input("How many chooks can you see in your backyard now? "))
yard_size = raw_input("And what kind of yard have you got? (Big, Small) ")
print

chook_shed(chook_factor, yard_size)

print
print

print "=================================================="