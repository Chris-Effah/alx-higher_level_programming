#!/usr/bin/python3
for char_code in range(ord('Z'), ord('A') - 1, - 1):
    print("{}".format(chr(char_code).lower() if char_code % 2 == 1
                    else chr(char_code).upper()), end="")
