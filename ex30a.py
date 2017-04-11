#  -*- coding: utf8 -*-
# Exercise 30: Else and If

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 30a: Else and If extension on errors in logic"

print
print

# 

print "We're testing to see what various values do to incorrectly written tests."
a = raw_input("Value for a? ")
b = raw_input("value for b? ")

print """
a = %s
b = %s
""" % (a, b)


print

# Note Well: if the two conditions are the same, python will just get
# confused about which action to perform.
 
if b > a:
    print "python chooses if b > a"
elif b > a:
    print "python chooses elif b > a"
else:
    print "python chooses else everything else"

print

print "======================================================================="