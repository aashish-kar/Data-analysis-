# Functional Programming
# Programming by the use of the functions

# Use of functions makes our code structured
# Functions helps in code re-using
# FUnction reduces the code repetation
# DRY => DOnt Repeat Yourself


# By only defining a function doesnot works
# Syntax for defining the function
# def function_name(parameters):
#     code to be executed

# We need to call the function
# function_name(arguments)

# Arguments => Arguments are the values sent to the function
# Parameters => The variables that receives the arguments 

# Eg: Function without parameters and arguments
# def display():
#     print("I am Ujjwal Neupane")
    
# display()

# EG: Function with parameters and arguments
# def sum(a,b):
#     print(f"Addition is {a+b}")
# fstring => Formatted string
# f"Combines string and {variables}"
    
# sum(5,10)

# Builtin Functions
# The functions that are pre build in Python
# We just need to use the built in functions
# print(), input(), int(), list(), dict(), tuple()

# User defined functions
# Functions created by the programmer
# sum(), display()

# Returnable function
# The function that returns some value
# return keyword is used in returnable function 
# def sum(a,b):
#     return a-b

    
# result = sum(10,5)
# print(result)

# def sum(a,b):
#     return
    
# result = sum(5,10)
# print(result)
# The function returns the value at the place from where it is being called
# if a function returns a value, we need a variable to store the returned value

# Non returnable function
# FUnction that doesnot returns any value
# def sum(a,b):
#     print(f"Addition is {a+b}")
# fstring => Formatted string
# f"Combines string and {variables}"
    
# sum(5,10)


# Types of Arguments
# Positional Arguments ( args)
# If the parameters receives the value based on the position, it is called positional arguments.
# Positional Arguments are denoted by *

# Keyword Arguments( kwargs)
# Keyword arguments are provided in key=value pair
# Positional Arguments are denoted by **
# Position doesnot matters in kwargs

# def sum(a,b):
#     return a-b

    
# result = sum(b=5, a=10)
# print(result)

# Positional Arguments and Keyword arguments in a same function

# def abc(*args, **kwargs):
#     # print(f"Args = {args}")
#     # print(f"Kwargs = {kwargs}")
#     return args, kwargs

# args,kwargs = abc(5,4,6,7,98,7,8,2,5,4,"Ujjwal","ABC", a=1,b=5, c="Ujjwal", d="Neupane")
# print(args)
# print(kwargs)

# Calculator program using function

def operation(method):
    num1 = int(input("ENter number 1: "))
    num2 = int(input("ENter number 2: "))
    if method == 'add':
        print(f"Addition is {num1+num2}")
    if method == 'subtract':
        print(f"Subtraction is {num1-num2}")
        

while True:
    choice = input("Enter 1 for addition, 2 for subtraction, 3 for exit: ")
    if choice == '1':
        operation('add')
    elif choice == '2':
        operation('subtract')
    elif choice == '3':
        print("Exiting")
        break
    else:
        print("Invalid Input")
        
# TAsk: Update calculator, login register program using function