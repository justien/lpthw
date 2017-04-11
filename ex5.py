# Describe Zed Shaw - the Hard Way!

# -*- coding: utf-8 -*-

# here we define our variables

my_name = "Zed Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # pounds
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# now we print out information about Zed, using the above defined variables

print
print 
print " . . . . . . . . . . . . . . . . . "
print "Describe Zed Shaw - the Hard Way!"
print
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# now Zed wants us to really concentrate on typing a tricky line 
# that shows us we are adding similar types together.
# this probably wouldn't work if we used %d and %s together.

print "If I add %d, %d, and %d - I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight) 

print
print
