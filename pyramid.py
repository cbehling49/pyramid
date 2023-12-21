"""
Cody Behling
CS-1410-602

Project 2 - Human Pyramids
The purpose of this assignment is to become familiar with recursion and solve a problem that is inherently recursive.
(i.e., It is difficult to figure out how to do it with loops and no recursion.)

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating.
I will receive a zero on this project if I am found in violation of this policy.
"""

# import necessary libraries
import sys
from time import perf_counter

# modular-level variables
indWeight = 200
functionCounter = 0
cacheCounter = 0
cache = {}


# recursive function
def weight_on(r, c):
    # import variables from modular level
    global functionCounter
    global cacheCounter

    # count function calls and cache hits
    functionCounter += 1
    if (r, c) in cache:
        cacheCounter += 1
        return cache[(r, c)]

    # base case and three additional cases
    if r == 0:
        result = 0.00
    elif c == 0:
        result = (indWeight + weight_on(r-1, c)) / 2
    elif r == c:
        result = (indWeight + weight_on(r-1, c-1)) / 2
    else:
        result = (indWeight + (weight_on(r-1, c-1) + weight_on(r-1, c)) / 2)

    cache[(r, c)] = result
    return result


def main(rows=7):
    # begin timer
    start = perf_counter()
    # create new file for output data
    with open('part3.txt', 'a') as output:
        for i in range(rows):
            for j in range(i + 1):
                line = ("%.2f" % weight_on(i, j))
                output.write(f"{line} ")
            output.write("\n")
        # end timer
        stop = perf_counter()
        output.write(f"\nElapsed time: {stop - start} seconds")
        output.write(f"\nNumber of function calls: {functionCounter}")
        output.write(f"\nNumber of cache hits: {cacheCounter}")


if __name__ == '__main__':
    # validate number of rows to be analyzed
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
