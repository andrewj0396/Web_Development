#!/usr/bin/python3

import sys

todo_list = []
#Read the contents of todo list text file todo_list
with open("todo's.txt") as r_file:
    todo = r_file.readline()
    while todo:
        todo = todo.strip()
        todo_list.append(todo)
        todo = r_file.readline()

if sys.argv[1] == '0':
    del todo_list[0]

print(todo_list)

todo_text = "\n".join(todo_list)

with open("todo's.txt", "w") as open_file:
    open_file.write(todo_text)
