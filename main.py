# ToDoGen Project
# By RDIL
# Under the MIT License
import os.path
import sys

print("Welcome to the To-do gen.  How this is going to work is there are going to be 20 slots, and you have to fill")
print("each one with something.  Once you put something in them, press enter.  You may leave some blank.  ")
print("")

maximumInputSize = input("TODO list size? ")
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
sys.exit("Program Ended.")
