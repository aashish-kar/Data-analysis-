# Data Types in Python

# Tuple 
# Tuple is an ordered and immutable data type
# Tuple is wrapped with ()

# NEsted tuple => Tuple inside the tuple
# tuple1 = (1, 2, 3, "Ujjwal", True, (1, 2, 3, "Ujjwal", True), [1, 2, 3, "Ujjwal", True], {"name": "Ujjwal", "age": 22})
# print(tuple1)

# Set
# Set is an unordered and mutable data type
# Set is wrapped with {}
# Set cannot contain duplicates

# set1 = {1, 2, 3, "Ujjwal", True,"Neupane", 1,2,3,"Ujjwal"}
# print(set1)


# DIctionary
# DIctionary is an unordered datatye but it is mutable
# Elements comes in key:value pair
# DIctionary also wrapped with {}

# dict1 = {
#     "name": "Ujjwal",
#     "age": 22,
#     "list" : [1, 2, 3, "Ujjwal", True],
#     "tuple" : (1, 2, 3, "Ujjwal", True),
#     "set" : {1, 2, 3, "Ujjwal", True},
#     "dict2" : {
#         "name": "Ujjwal",
#         "age": 22,
#         "list" : [1, 2, 3, "Ujjwal", True],
#         "tuple" : (1, 2, 3, "Ujjwal", True),
#         "set" : {1, 2, 3, "Ujjwal", True}
#     }
# }

# print(dict1)

"""
Create a dictionary of usernames and password
"""
# dict1 = {
#     "Ujjwal" : "Ujjwal@123",
#     "Neupane" : "Neupane@123",
#     "Sujan" : "Sujan@123",
#     "Harit" : "Harit@123",
#     "Sujal" : "Sujal@123"
# }



# Create a list of usernames
# Ask the username from the user
# Print login successful if username is present in list
# else print login failed
# usernames = ["Ujjwal", "Ram", "Hari", "ABC"]
# user_input = input("ENter your username: ")
# print(user_input in usernames)





# Conditional Statements
# Those statements that will be executed according to the condition
# IF-ELSE
# match
# LOOPS

# IF ELSE
# if condition:
#     # If condition is True, code to be executed
# else:
#     # If condition is False, code to be executed

# age = 10

# simple if else
# if age > 18:
#     print("You are a voter")
# else:
#     print("You are a non voter")

# WHen you need to execute sth only if condition is True
# You could use simple if

# Simple if
# age = 8
# if age > 10:
#     print("Your age is grater than 10")

# Elif ladder
# Elif ladder is used when you have multiple conditions

percentage = int(input("ENter your percentage: "))
if percentage >= 90:
    pass
elif percentage >= 80 and percentage < 90:
    pass
elif percentage >= 70 and percentage < 80:
    print("B+")
elif percentage >= 60 and percentage < 70:
    print("B")
elif percentage >= 50 and percentage < 60:
    print("C+")
else:
    print("Failed")
    
    
# Nested if else
# Find the greatest number among 3 numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 > num2:
#     if num1 > num3:
#         print("Num1 is greater ", num1)
#         if num2 > num3:
#             if num2 > num3:
#                 pass
#             else:
#                 pass
#         else:
#             if num2 > num3:
#                 pass # => pass does nothing
#             else:
#                 pass
#     else:
#         print("Num3 is greatest ", num3)
# else:
#     if num2 > num3:
#         print("num2 is greatest ", num2)
#     else:
#         print("num3 is gratest ", num3)
        