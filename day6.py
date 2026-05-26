# Function types

# Lambda Function
# The function of one line is called lambda function
# Lambda function is called nameless function because 
# while defining the lambda function we dont give a name
# We need name to call lambda function
# Lambda always returns a value
# Syntax:
# lambda parameters : operation

# sum = lambda a,b:print(a+b)
# sum(5,7)

# Map function
# Map function takes a function and group data type as an argument
# Map applies the function to each element of group data type
# Syntax
# map(function, group_data_type)

list1 = [1,2,3,4,5,6]

# print(list(map(lambda x : x*2, list1 )))

# Filter function
# Filter function takes a function and group data type as an argument
# Filter function filters out the elements from group data type according to our condition
# SYntax
# filter(function with condition, group data type)

# print(list(filter(lambda x : x%2==1, list1)))

# Reduce merges the element of group data type into a single value
# Reduce also takes function and group datatype as an argument
# SYntax:
# from functools import reduce
# reduce(function, group data type)

# print(reduce(lambda x,y : x+y, list1))

# Zip function
# Zip combines multiple group data types into a combined tuple

# names = ["Ujjwal", "Ram", "Shyam", "Hari"]
# age = [25,26,27,24]
# marks = [98,96.56,56,88.2]
# # SYntax
# # zip(group_datatype1, group_datatype2, ..., group_datatypen )

# print(list(zip(names,age,marks)))


# Login and register program by using username and password
usernames = []

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        dict_cred = {username:password}
        usernames.append(dict_cred)
        print("Registration Successfull")
    if method == 'login':
        for cred in usernames:
            if username in  cred and cred[username] == password:
                print("Login Successfull")
                break
        else:
            print("Login Failed")
                
# FOR ELSE
# IF break encounters in for block, it exits the complete loop (it exits the else part also)
# Else, else part only is executed
            
        

while True:
    choice = input("ENter 1 for register, 2 for login, 3 for exit:  ")
    if choice == '1':
        operation('register')
    elif choice == '2':
        operation('login')
    elif choice == '3':
        print("Exiting")
        break
    else:
        print("Invalid input")
        
# Research task
# After successful login, show thw atm menu (view balance, add balance, withdraw balance)
# # USe while loop 
# if user says add balance, current balance + amount 
# if user says withdraw balance, current balance - amount
# if user says view balance, display the current balance
# if user says exit, exit from atm menu
# else print invalid input

# Task: Update it so a user cannot register twice from same username