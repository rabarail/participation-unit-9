"""Rajani Baraili, March 15, 2026,
prints random number between 1 and 6 and rolls."""

import random

class Die:
    sides = 6
    def roll_die(self):
        return random.randint(1, self.sides)
die = Die()
for i in range(10):
    print(f"6 sides - Rolling the die ... {die.roll_die()}")

die = Die()
die.sides = 10
for i in range(10):
    print(f"10 sides - Rolling the die ... {die.roll_die()}")
die = Die()
die.sides = 20
for i in range(10):
    print(f"20 sides - Rolling the die ... {die.roll_die()}")