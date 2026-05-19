#comments in python
#comments are the programmers notes to explain the code
# ide ignores the comments
#in python, # as prefix is used for sinfle line comments
#for multiline commetns, we can use tripple quotes(''' or """)


#variable = programmer defined area to store data
# python variable can store any data type

#name ="aashish"
#print (name)

#naming convention in python
#way of giving names to the variables
#1 PascalCase - each word starts with capital letter
#2 camelCase - first word starts with small letter and rest of the words start with capital
#3 snake_case - all words are in small letter and separated by underscore
#4 kebab-case - all words are in small letter and separated by hyphen (not allowed in python)

#variable naming rules in python
#1 variable name should start with a letter or underscore
#2 variable name can contain letters, digits and underscores
#3 variable name cannot contain spaces
#4 variable name should reflect the content of the variable
#5 keywords cannot be used as variable names

#input()
#input{"message to be displayed to the user"}
#input() function is used to take input from the user
# and we need a variable to store the input from the user
#input receives data in string

#name = input("enter your name: ")
#print("hello", name)

#simple program to add two numbers
#num1 = input("enter first number: ")
#um2 = input("enter second number: ")
#print("the sum is: ", num1 + num2) # this will concatenate the two numbers as strings


#type casting - converting one data type to another
#the process of converting one data type to anothher data type is called type casting
# # datatypes => int, float, str, 

#type() function is used to check the data type of a variable
num1 = input("enter first number: ")
num2 = input("enter second number: ")
print("the sum is: ", num1 + num2) # this will concatenate the two numbers as strings
# to perform addition, we need to convert the input from string to int
num1 = int(num1)
num2 = int(num2)
print("the sum is: ", num1 + num2) # this will perform addition and
print("the sum is: ", str(num1 + num2)) # this will convert the result back to string and print it
