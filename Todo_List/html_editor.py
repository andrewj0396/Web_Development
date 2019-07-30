#!/usr/bin/python3
#This script reads todos from a basic text file and then populates an html file accoringinly

import sys
import re

#Initialize empty todo_list
todo_list = []

#Read the contents of todo list text file todo_list
with open("todo's.txt") as r_file:
    todo = r_file.readline()
    while todo:
        todo = todo.strip()
        todo_list.append(todo)
        todo = r_file.readline()

#Open and read from the index HTML file.
with open("index.html") as index:
    page_text = index.read()

#First check if there is already a set of list items in there
if "<li>" in page_text:
    #If there are list items use regex to make a list of those lines called lines_to_replace
    lines_to_replace = re.findall(r'<li>(.*?)</li>', page_text)
else:
    lines_to_replace = ""

#print(lines_to_replace)
#print(type(todo_list[0]))

#Take the elements of lines_to_replace, reformat them, then replace them within the page_text text string
for line in lines_to_replace:
    #Add <li> and </li> tags to line (the regex above doesn't incluede those)
    newLine = "<li>{:s}</li>".format(line)
    #print(newLine)
    #Replaces the top line with the HTML comment tag
    if lines_to_replace.index(line) == 0:
        page_text = page_text.replace(newLine, "<!--list-->")
    #Replaces all other lines with an empty string
    elif lines_to_replace.index(line) > 0:
        page_text = page_text.replace(newLine, "")

#Removes newlines
page_text = re.sub(r'\n\n\n\n\s+', ' ', page_text)
#print(page_text)

#print(todo_list)

#Removes the todo elements which are passed in as arguments from php
todones = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]

#This for loop weeds out the todones from the list of todos
for element in todones:
    if element in todo_list:
        del todo_list[todo_list.index(element)]

#formatts the todo into and writes them to the todo list file
todo_text = "\n".join(todo_list)
#print(todo_text)
#'''
with open("todo's.txt", "w") as open_file:
    open_file.write(todo_text)
#'''

#Prepare string of HTML list items to be injected into html file b/w <ul> tags
html_list = ''

for todo in todo_list:
    #print(type(todo_list.index(todo)))
    html_list += '<li>{:s}{:s}      <input type="checkbox" name="item[]" value="{:s}"></li>\n'.format(todo, ":", todo)#(todo_list.index(todo)+1)
#print(html_list)

#Replace the empty <ul> tags in the page_text with the newly formatted string
page_text = page_text.replace("<!--list-->", html_list)
#print(page_text)
#'''
#Write the changed html code back to the index.php file
with open("index.html", "w") as open_file:
    open_file.write(page_text)
#'''
