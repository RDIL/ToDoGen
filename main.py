# ToDoGen Project
# By RDIL, PelajTech
# Under the MIT License

import os
import sys

maximumInputSize = input("Number of TODO list items: ")
currentInputIndex = 0

currentRetrievedText = ""

todos = {}

while currentInputIndex < int(maximumInputSize):
    currentInputIndex += 1
    currentRetrievedText = input(str(currentInputIndex) + ". ")

    todos.update({str(currentInputIndex): currentRetrievedText})

if os.path.exists("ToDoList.txt") and os.path.isfile("ToDoList.txt"):
    open('ToDoList.txt', 'w')

todoFile = open("ToDoList.txt", "a")

todoFile.write("\n")
for key, value in todos.items():
    todoFile.write(key + ". " + value + "\n")

todoFile.close()

if os.name == "nt":
    # Windows
    os.system("start ToDoList.txt")

elif os.name == "posix":
    # Linux
    os.system("xdg-open ToDoList.txt")
    
sys.exit("Program finished.")

