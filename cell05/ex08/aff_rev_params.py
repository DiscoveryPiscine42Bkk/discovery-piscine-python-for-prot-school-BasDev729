#!/usr/bin/env python3
import sys

# Check if there are at least two parameters
if len(sys.argv) > 2:
    print(" ".join(sys.argv[1:][::-1]))  # Reverse and print parameters
else:
    print("none")  # Print "none" if fewer than two parameters
