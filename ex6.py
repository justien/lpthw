# -*- coding: utf-8 -*-

# Strings and Text

print 
print

print "=========================================="

print "Strings and Text"

print
print

# Here we introduce four strings: x, y, binary, and do_not.
# binary and do_not are simple name-to-value string mappings.
# x is a string where part of its value is another string.
#     x is a string that contains a string.
#     This second string's value is supplied immediately on the same line.
# y is a string which contains two strings.
#    These two strings are themselves strings, so it's a double-hop to the final value.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print

# Now we have two print statements that use strings.
# The first statement asks for r, which asks for x, which asks for d, which is the number value 10
# That's a triple-hop.
# The second statement asks for s, which asks for y, which asks for another s, which ask for binary and do_not
# That's a quadruple-hop.

print "I said: %r." % x
print "I also said: '%s'." % y

print

# Erkay - here're two string substitutions.
# The first is just an equality.
# The second is also an equality, that contains a pointer to a string.
# However, the string is not evaluated at this point.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# ... until we get to here, where the juxtaposition of the
# two strings in the right order results in a meaningful python statement.

print joke_evaluation % hilarious

print

# Notable here is that the plus operator gets rid of whitespace 
# being inserted on either side of the concatenation.

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print

print "=========================================="
