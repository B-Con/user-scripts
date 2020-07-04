#!/bin/python3
import sys


TARGET_RATIO = 1.777777


def findScale(x, y):
    x = 1.0 * int(x)
    y = 1.0 * int(y)
    new_x = x
    new_y = y
    
    # These ratios allow for one pixel of deviation on either side.
    if x / y > 1.7788:
        new_x = y * TARGET_RATIO
        print("resize x = {}".format(new_x))
    elif x / y < 1.776:
        new_y = x / TARGET_RATIO
        print("resize y = {}".format(new_y))
    else:
        print("correct size")


def main():
    findScale(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()

