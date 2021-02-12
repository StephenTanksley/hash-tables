# Your code here

import random
import math
import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


# instantiate the table.
table = {}


# Create a helper function to build out the lookup table.
def build_table():

    # Build the table by using the same parameters as the main function below.
    for x in range(2, 14):
        for y in range(3, 6):
            table[(x, y)] = slowfun_too_slow(x, y)

    return table


lookup_table = build_table()


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    return lookup_table[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
