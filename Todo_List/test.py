#!/usr/bin/python3
#test script

import sys

list = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]

text = "".join(list)
#print(text)

with open("file.txt", "w") as open_file:
    open_file.write(text)
