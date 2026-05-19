# Simple calculator

name = input("Enter your name:")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

print(name + "'s calculator:")
print("addition:", num1 + num2)
print("subtraction:", num1 - num2)
print("multiplication:", num1 * num2)
print('division:', num1 / num2)
print("remainder:", num1 % num2)
print("power:", num1 ** num2)