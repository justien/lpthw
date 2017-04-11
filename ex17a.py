#  -*- coding: utf8 -*-
# Exercise 17: More Files extension

# 23456789012345678901234567890123456789012345678901234567890123456789

print "=================================================="
print "Exercise 17: More Files extension"

print
print

# Now we're going to do Ex17 work on one line.
# Much rad and compress.

from sys import argv
from os.path import exists

script, from_file, to_file = argv


open(to_file, 'w').write(open(from_file).read())

# As you can see, these methods can act directly on each other.
# It's not necessary to stage each type of object as a string
# before operating them all together.

# one concern - with this one liner, neither from_file nor to_file
# have been closed.


print
print

print "=================================================="