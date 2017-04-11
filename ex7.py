# -*- coding: utf-8 -*-

# Exercise 7: More Printing

print 
print

# int "01234567890123456789012345678901234567890123456789
print "=================================================="

print "More Printing"

print
print

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' 
#                                      ^^^^^ the string is snow, so outputs snow
print "Its fleece was white as %r." % 'snow' 
#                                      ^^^^^ this is taken as raw input, so outputs 'snow'
print "And everywhere that Mary went."
print "." * 10 #what'd that do?

end1 = "C" * 10
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r" * 10

print
print

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

print "%s, %s, %s, %s, %s, %s" % (end1, end2, end3, end4, end5, end6) * 2

print 
print

print "=================================================="
