#  -*- coding: utf8 -*-
# Exercise 10: What was that?

print "=================================================="
print "Exercise 10: What was that?"

print
print

# here are the defined strings, including:
#    * the use of \t to show a tab indentation
#    * the use of \n to show a new line
#    * the use of \ to escape the following '\' so it is printed

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"
furry = "cat brush"


# fat_cat is a multi-line string, and uses \t to have nice formatting

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies (cat's favourite!)
\t* Catnip
\t* Grass\n\t* Grackle
'''


# furry_cat shows you how to escape the percentage sign so it can be printed

furry_cat = """
furry_cat needs 10%% time with\n\t* %s
""" % furry

print tabby_cat

print

print persian_cat

print

print backslash_cat

print

print fat_cat

print

print furry_cat

print
print

print "=================================================="
