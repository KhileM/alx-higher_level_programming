#!/usr/bin/python3

import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    arguments = sys.argv[1:]

    print("Number of argument(s):", num_arguments)
    if num_arguments == 0:
        print(".", end="\n\n")
    elif num_arguments == 1:
        print("Argument:", arguments[0])
        print("1:", arguments[0])
    else:
        print("Arguments:", end="\n\n")
        for i, argument in enumerate(arguments, start=1):
            print(f"{i}: {argument}")

print_arguments()
