# LOOPS
# Loops are used when we need to execute the same block of code again and again

# There are 2 types of loops in python: for loop, while loop

# for loop is used when we know the start and stop condition
# while loop is used when we dont know the start and stop condition

# Syntax for for loop

# for iterator in iterable:
#     code to be executed

# iterator => The variable used to store the current value when loop is running
# iterable => The group data type where the loop runs
# iteration => One complete cycle of loop

# list1 = {"name":"Ujjwal",
#          "age":27,
#          "marks":96.5
#         }
# for i in list1:
#     print(i)
    
# range(start, end, step) => range() creates the sequence of numbers
# range() is used in loop
# for i in range() 

# for i in range(15):
#     print(i)
# if only one value is provided inside range(), it is for end, start is always 0
# end value is always exclusive, start is always inclusive

# for i in range(5,15):
#     print(i)
# if 2 values are provided in range, first value will be for start and second value will be for end

# for i in range(0,15,3):
#     print(i)
    
# if 3 values are provided, start, end, step


# break and continue
# Can only be used inside the loop

# break => When break ecounters, it exits from the current loop
# continue => WHen continue encounters, it skips the current iteration but doesnot exit from the loop

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# SYntax for while

# while condition:
#     code to be executed

# Problem => Infinite Loop

# Update the calculator program using loop and if else

credentials = ""

while True:
    choice = input("Enter 1 for login, 2 for register, 3 for exit: ")
    if choice == '1':
        username = input("Enter your username: ")
        if username in credentials:
            print("Login Successfull")
        else:
            print("Login Failed")
    elif choice == '2':
        username = input("Enter your username: ")
        credentials.append(username)
        print("Username Registered")
        print(credentials)
    elif choice == '3':
        break
    else:
        print("Invalid Input")
        

print("Out of the system")      
        
