#  -*- coding: utf8 -*-
# Exercise 26: Take a Test

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 26: Take a Test"

print
print

from ex26_defs import *

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

raw_input('Press any key to print the poem')

print "--------------"
print poem
print "--------------"


raw_input('Press any key to print the variable \'five\' ')


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


raw_input('Press any key to talk about jelly beans')


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


raw_input('Press any key to create and print the sentence')
sentence = "All good things come to those who wait."
print sentence

raw_input('Press any key to make the sentence iterable and sorted')
words = make_a_list_from(sentence)
sorted_words = sort_words(words)

raw_input('Press any key to print the first word of the sentence')
print_first_word(words)

raw_input('Press any key to print the last word of the sentence')
print_last_word(words)

raw_input('Press any key to print the first word of the sorted list')
print_first_word(sorted_words)

raw_input('Press any key to print the last word of the sorted list')
print_last_word(sorted_words)

raw_input('Press any key to recreate the original, non-popped list')
sorted_words = sort_sentence(sentence)

raw_input('Press any key to print this newly recreated list')
print sorted_words

raw_input('Press any key to print the first and last words of the unsorted sentence')
print_first_and_last(sentence)

raw_input('Press any key to print the first and last words of the sorted sentence')
print_first_and_last_sorted(sentence)


print
print

print "======================================================================="