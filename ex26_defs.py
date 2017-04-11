#  -*- coding: utf8 -*-
# Exercise 26 definitions: Take a Test

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

print "========================================================================"
print "Exercise 26 definitions: Take a Test"

print
print

def make_a_list_from(stuff):
    """This function will create an iterable list from the input sentence."""
    words_list = stuff.split(' ')
    return words_list

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    first_word = words.pop(0)
    print first_word

def print_last_word(words):
    """Prints the last word after popping it off."""
    last_word = words.pop(-1)
    print last_word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = make_a_list_from(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = make_a_list_from(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)