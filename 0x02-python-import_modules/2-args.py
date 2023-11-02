#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
countAv = len(arguments)
if countAv == 1:
    print(f"{countAv} argument:")
elif countAv > 1:
    print(f"{countAv} arguments:")
else:
    print(f"{countAv} arguments.")

for i, arg in enumerate(arguments, start=1):
    print(f"{i}: {arg}")
