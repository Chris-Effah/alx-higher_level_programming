#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_of_args = 0
    for i in range(len(sys.argv) - 1):
        sum_of_args += int(sys.argv[i + 1])
    print("{}".format(sum_of_args))

