#  -*- coding: utf8 -*-
# Exercise 32: Making Decisions

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 32: Making Decisions"

print
print

print """
You enter a dark room with two doors. 
Do you go through door #1 or door #2?
"""

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cake. what do you do?"
    print "1. Take the cake."
    print "2. Surprise the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "the bear is very focussed on eating cake, so eats you too."
    elif bear == "2":
        print "bear does not enjoy the surprise, and pushes you to the floor."
    else:
        print "Yes. %s is a better thing.  Bear exits the scenario." % bear
        
elif door == "2":
    print "You stare into the endless abyss."
    print "1. Blueberries from the forest."
    print "2. Clothespins made of wasps."
    print "3. Gunfire's song is your song now."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives with a mind half in the past, half in the sun."
    else:
        print "The insanity becomes part of your hands and eyes,\na new fifth limb of perception."
        
else:
    print "You stumble around.  There is a knife, which you take on your journey into the dustlands."
	

print
print

print "======================================================================="