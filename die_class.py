"""Rajani Baraili, March 15, 2026,
prints random number between 1 and 6 and rolls."""

import random

class Die:
    sides = 6
    def roll_die(self):
        return random.randint(1, self.sides)
