# Comparison Operators
# Used to compare two values and return a boolean value
# boolean => True or False
# > => greater than
# < => less than
# >= => greater than or equal to
# <= => less than or equal to
# == => checks the value of the variable
# != => checks if the value of the variable is not equal to another value

# print(10 > 5)
# print(10 < 5)
# print(10 >= 5)
# print(5>=5)
# print(10 <= 5)
# print(10 == 5)
# print(10 != 5)

# Logical Operators
# Used to combine two or more conditions and return a boolean value
# and, or , not


# Membership Operators
# Used to check if a value is present in a group data type or not
# in, not in

# Group Data Type
# The data type in Python that contains multiple elements
# str => Str contains multiple characters
# name = "Ujjwal"
# print("u" not in name)

# List
# Tuple
# Set
# DIctionary


# Identity Operators
# Identity operator and == does the same thing
# But the difference is, identity operator checks the memory location of the variable
# is, is not
# a = "Ujjwal"
# b = "Ujjwal"
# a = ["Ujjwal","Neupane", 1, 2, 3]
# b = ["Ujjwal","Neupane", 1, 2, 3]
# c = a
# print(a is b)
# print(a == b)
# print(a is c)
# print(a is not b)
# print(a == b)
# print(a is not c)

# Data Types
# Built-in => int, float, str, bool, list, tuple, set, dictionary

# Types of Data Types
# 1. Mutable Data Type
# The data type that can be changed after it is created 
# Original object is changed

# 2. Immutable Data Type
# The data type that cannot be changed after it is created
# If the data type nedds to be changed, python creates a new object
# int, float, str, bool


# String
# Anything wrapped with " ", '', or ''' or """
# eg: "Ujjwal", 'Ujjwal', '''Ujjwal''', """Ujjwal"""

# LIST
# A collection of multiple elements wrapped with []
# EG: [1, 2, 3, "Ujjwal", True]
# List can contain element of any data type
# List is a mutable data type
# List is a ordered data type
# list1 = [1, 2, 3, "Ujjwal", True]
# print(list1)

# Nested List => List inside the list
list1 = [1, 2, 3, "Ujjwal", True, [1, 2, 3, "Ujjwal", True]]
print(list1)