#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit == 8 and ones_digit == 9:
            print("{}{}".format(tens_digit, ones_digit))
        else:
            print("{:02d}".format(tens_digit * 10 + ones_digit), end=", ")

