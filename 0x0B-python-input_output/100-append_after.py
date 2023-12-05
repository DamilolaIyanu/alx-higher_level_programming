#!/usr/bin/python3
"""inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text file"""
    with open(filename, "r", encoding='utf-8') as f:
        llist = []
        while True:
            line = f.readline()
            if line == "":
                break
            llist.append(line)
            if search_string in line:
                llist.append(new_string)
    with open(filenamen, "w", encoding="utf-8") as f:
        f.writelines(llist)
