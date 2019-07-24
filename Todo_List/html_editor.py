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
with open("index.php") as index:
    page_text = index.read()

#First check if there is already a set of list items in there
if "<li>" in page_text:
    #If there are list items use regex to make a list of those lines called lines_to_replace
    lines_to_replace = re.findall(r'<li>(.*?)</li>', page_text)
else:
    lines_to_replace = ""
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

#Check if an entry has been replaced
def editToDos(todoIndex):
    if todoIndex == '0':
        del todo_list[0]

#editToDos(sys.argv[1])

#print(todo_list)

todo_text = "\n".join(todo_list)

with open("todo's.txt", "w") as open_file:
    open_file.write(todo_text)
#Prepare string of HTML list items to be injected into html file b/w <ul> tags
html_list = ''

for todo in todo_list:
    #print(type(todo_list.index(todo)))
    html_list += '<li>{:s}{:s}      <input type="submit" name="Test{:d}[]" value="remove"></li>\n'.format(todo, ":", todo_list.index(todo))
#print(html_list)

#Replace the empty <ul> tags in the page_text with the newly formatted string
page_text = page_text.replace("<!--list-->", html_list)
#print(page_text)

#Write the changed html code back to the index.php file
with open("index.php", "w") as open_file:
    open_file.write(page_text)