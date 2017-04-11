#  -*- coding: utf8 -*-
# Exercise 35: Branches and Functions

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 35: Branches and Functions"

print
print

from sys import exit

def gold_room():
    print "This room is full of gold. How many pots of gold do you take?"
    
    choice = raw_input("> ")
    if ("0" in choice or "1" in choice) and int(choice) < 50:
        print "Not too greedy! You WINNN!!"
        exit(0)
    elif ("0" in choice or "1" in choice) and int(choice) > 50:
        dead("All that gold is heavy, and the bear catches you as you leave.")
    else:
        dead("Srsly we only accept binary around here.")
        
def bear_room():
    print "There is a bear in here."
    print "The bear has a heap of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear reacts possessively towards the honey by eating you.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear has had enough of this, and chews your leg meditatively.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I don't understand what you're saying."
            
def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "As it observes you, you start to go insane."
    print "Do you flee for your life, or consume yourself?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Extremely delicious.")
    else:
        cthulu_room()
        
def dead(why):
    print why, "Good Game, Citizen!"
    exit(0)
    
def start():
    print "You are in a dark room."
    print "There is a door to your left and to your right."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room, and eventually starve.")
        
start()
    


print
print

print "======================================================================="