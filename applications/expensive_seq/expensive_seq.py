# Your code here


"""
    Problem: We have a very computationally expensive set of operations that we'd like to store values for so we don't need to look them up every time.
    
    Solution: We create a lookup table at the very beginning of the function. At the start of the function expensive_seq(), we look into our table to see if the solution already exists which use those arguments. If so, we can just return that result.
    
    Otherwise, we can just return the results of the expensive functions and store them in the table. We'll have to do the hard work at first to build the table, but it should get easier each time as we fill out more and more possibilities in the table.

"""

# We know we're gonna need a lookup table here, so we instantiate it here.
table = {}


def expensive_seq(x, y, z):

    # If the answer already exists, pull it from the table. This is O(1) lookup time, so this is preferable to having to generate the answer every time.
    if (x, y, z) in table:
        return table[(x, y, z)]

    # if x is less than or equal to zero, just add y and z as the result. This is our base case where we're exiting the recursive loop.
    if x <= 0:
        result = y + z

    # if x is greater than zero, we venture into a recursive area where we call the function inside the function and make progress towards the base case by decrementing x each time.
    if x > 0:
        result = expensive_seq(
            x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    table[(x, y, z)] = result

    return table[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
