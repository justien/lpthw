#  -*- coding: utf8 -*-
# Exercise 30: Else and If

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 30: Else and If"

print
print

# 

print "We need to get out of here.  The zombies are coming."
people = raw_input("How many people are there? ")
cars = raw_input("How many cars can you see out there? ")
trucks = raw_input("Trucks.  Tell me how many. ")

print "Ok, that's %s people, %s cars, and %s trucks." % (people, cars, trucks)
print "Here's what we'll do."

print

# Note Well: if the two conditions are the same, python will just get
# confused about which action to perform.
 
if cars > people:
    print "More cars than people!! We should take the cars."
elif cars < people:
    print "Ugh, cars outnumber the people. We should not take the cars."
else:
    print "We can't decide."

print

if trucks > cars:
    print "What? More trucks than cars?? That's too many trucks!"
elif trucks < cars:
    print " Ok - there are fewer trucks than cars. Maybe we could take the trucks."
else:
    print "We still can't decide."

print
    
if people > trucks:
    print "Alright, there are more trucks than people, let's just take the trucks."
else:
    print "Nope, more people than trucks, let's stay home."

print
print

print "======================================================================="