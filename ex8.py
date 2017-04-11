# -*- coding: utf-8 -*-
# Exercise 8: Printing, Printing

print "=================================================="
print "Printing, Printing"

print
print

# Formatter is a string, which text can be used as four values.
# It is a string that's made up of four raw inputs.
formatter = "%r %r %r %r"

# We now demonstrate that the value of the string conforms to python syntax.
# And by printing out exactly what is in the brackets (the supplied values),
# we can see that it is parsing the input as raw input.
# And that it can be used as a text source.
print formatter % (1, 2, 3, 4)
print
print formatter % ("one,", "two", "three", "four")
print
print formatter % (True, False, False, True)
print
print formatter % (formatter, formatter, formatter, formatter)
print
print formatter % (
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
print

# The last item of the following will be printed out with double-quotes,
# whereas the first 3 lines will print out with single quotes.
# I think this is because it contains a single quote, so the representation
# is shown in double quotes to (somehow) escape the single-quote.
print formatter % (
	"But it did not sing.",
	"But it did not sing.",
	"Nnn nn nnnnn nnnn.",
    "Nnn nn nnnn'n nnnn."
)

print "=================================================="
