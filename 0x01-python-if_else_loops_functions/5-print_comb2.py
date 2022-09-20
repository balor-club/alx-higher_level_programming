#!/usr/bin/python3
for num in range(0, 100):
    print("{:d}{:d}, ".format(num))
    num += num + 1
    print("{:d}{:d}".format(num))
