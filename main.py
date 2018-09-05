import sys

# ToDoGen Project
# By RDIL
# Under the MIT License

print("Welcome to the To-do gen.  How this is going to work is there are going to be 20 slots, and you have to fill")
print("each one with something.  Once you put something in them, press enter.  You may leave some blank.  ")

toDoOne = input("1. ")
toDoTwo = input("2. ")
toDoThr = input("3. ")
toDoFor = input("4. ")
toDoFiv = input("5. ")
toDoSix = input("6. ")
toDoSvn = input("7. ")
toDoEit = input("8. ")
toDoNin = input("9. ")
toDoTen = input("10. ")
toDoEle = input("11. ")
toDoTwe = input("12. ")
toDoThi = input("13. ")
toDoFrt = input("14. ")
toDoFft = input("15. ")
toDoStn = input("16. ")
toDoSen = input("17. ")
toDoEtn = input("18. ")
toDoNtn = input("19. ")
toDoTwt = input("20. ")

# Got To-Dos, now to write to file.

todo = open("ToDoList.txt", "a")

todo.write("\n")
