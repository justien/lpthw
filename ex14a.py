#  -*- coding: utf8 -*-
# Exercise 14a: Prompting and Passing - extension

print "=================================================="
print "Exercise 14a: Prompting and Passing - extension"

print
print

from sys import argv

script, user_name, leet_level= argv
prompt = "\n--->"

print "Welcome to %s." % (script)
print "%s, you have invoked leet level %s." % (user_name, leet_level)
print "I like you!  Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "\nI live in Berlin. Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "\nI use a Mac.  What sort of computer are you using?"
computer = raw_input(prompt)

print """
\nOK!  You said %s about liking me.  I respect that!
And thanks for sharing where you live  - %r.
And you're using a %r computer - nice!
""" % (likes, lives, computer)

print
print

print "=================================================="