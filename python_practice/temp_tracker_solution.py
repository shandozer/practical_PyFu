#!/usr/bin/env python
"""
Write a class TempTracker with these methods:

insert() records a new temperature
get_max() returns the highest temp  so far
get_min() returns the lowest temp  so far
get_mean() returns the mean of all temps  so far
get_mode() returns the mode of all temps so far. If there is more than one mode, return any of the modes.
get_mean() should return a float, but the rest of the getter functions can return integers.

Optimize for space and time.
Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode())
over speeding up the insert() function.


Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit,
so we can assume they'll all be in the range 0..1100..110.

__author__ = 'Shannon Buckley', 5/28/16
"""
import random


class TempTracker(object):

    def __init__(self):

        self.current_temp = random.choice(range(0, 111))

        self.temps_seen_so_far = [self.current_temp]

        self.new_temp = None

    def insert(self, n=None):

        self.new_temp = random.choice(range(0, 111))

        self.current_temp = self.new_temp

        self.temps_seen_so_far.append(self.new_temp)

        if n:
            for i in range(0, n):
                self.insert()

    def get_max(self):

        return max(self.temps_seen_so_far)

    def get_min(self):

        return min(self.temps_seen_so_far)

    def get_mean(self):

        return sum(self.temps_seen_so_far)/len(self.temps_seen_so_far)

    def get_mode(self):

        sorted_temps = sorted(self.temps_seen_so_far)

        num_temps = len(sorted_temps)

        mode = sorted_temps[num_temps/2]

        return mode


t = TempTracker()


print t.current_temp


t.insert()
t.insert(3)
t.insert(10)

print t.current_temp

print t.temps_seen_so_far

print t.get_max()
print t.get_min()
print t.get_mean()

print t.get_mode()
