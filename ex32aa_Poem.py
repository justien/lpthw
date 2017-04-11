#  -*- coding: utf8 -*-
# Exercise 32: Loops and Lists - Poem

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 32: Loops and Lists - making a list from a range, and a Poem"

print
print

# Zed would like to us to figure out how to avoid the following for-loop
# altogether, and instead assign range(0,6) directly to elements.

elements = [range(-2, -10, -1)]

# now we print them out too
for i in elements:
    print "Element was: %r" % i 

print

# Here's a very cool example from the pydoc online:

# poem					<-- is a list
# len(poem)				<-- count the number of elements in poem
# range(len(poem))		<-- a sequence as long as poem, start 0, step 1
# for i	in range()		<-- a loop using this range sequence
# print i, poem(i)		<-- print index count and the i-th element of poem

poem = ['On a building site', 'a sand heap gently settled.', 'I, walking by, watched.']
for i in range(len(poem)):
    print i, poem[i]



print
print

print "======================================================================="	