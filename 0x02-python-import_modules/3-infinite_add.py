#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    countArgs = len(sys.argv)
    for i in range(countArgs - 1):
        sum += int(sys.argv[i + 1])
    print(sum)
