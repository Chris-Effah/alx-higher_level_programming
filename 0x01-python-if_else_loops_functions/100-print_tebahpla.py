#!/usr/bin/python3
for c in range(ord('Z'), ord('A') - 1, - 1):
    print("{}".format(chr(c + 32 if c % 2 == 0 else c)), end="")
