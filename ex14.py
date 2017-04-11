#  -*- coding: utf8 -*-
# Exercise 14: Prompting and Passing

print "=================================================="
print "Exercise 14: Prompting and Passing"

print
print

from sys import argv

script, user_name = argv
prompt = 'A VERY DIFFEReNT SLICE OF 3.1415 --->'

print "Hallo %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "I like you!  Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "I live in Berlin. Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "I use a Mac.  What sort of computer are you using?"
computer = raw_input(prompt)

print """
OK!  You said %s about liking me.  I respect that!
And thanks for sharing where you live  - %r.
And you're using a %r computer - nice!
""" % (likes, lives, computer)

print
print

print "=================================================="
