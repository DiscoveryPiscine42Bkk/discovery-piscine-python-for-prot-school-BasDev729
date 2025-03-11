#!/usr/bin/env python3
import sys

# Check if exactly two parameters are provided
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.count(keyword)
    print(count if count > 0 else "none")
else:
    print("none")  # Print "none" if the number of parameters is not 2