#!/usr/bin/env python
"""
__author__ = Shannon B., 5/29/16

Write a recursive function for generating all permutations of an input string. Return them as a set.
Don't worry about time or space complexity; if we wanted efficiency we'd write an iterative version.
To start, assume every character in the input string is unique.
Your function can have loops; it just needs to also be recursive.
"""


def permute_string(input_string):
    permutations = []

    i = 1

    while i < len(input_string):
        permutations.append(input_string[0:i])

        permute_string(input_string[0:i])

        i += 1

    return set(permutations)

set_of_strings = permute_string('this is a test string')

print sorted(set_of_strings)
