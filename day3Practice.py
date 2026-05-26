# username login system
username = ["Aashish","Aaruph","Saurav"]
user_input =input("Enter your username:")
if user_input in username:
    print("Login secessful")
else:
    print("Login failed")

#grade calculator
percentage= int(input("Enter your percentage:"))
if percentage >= 90:
    print("Grade:A")
elif percentage >= 80:
    print("Grade :B+")
elif percentage >=70:
    print("grade: B")
elif percentage >=60:
    print("grade:c+")
elif percentage >=50:
    print("grade:c")
else:
    print("failed")

#greatest of 3 number
num1= int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3= int (input("Enter Third number:"))
if num1>num2 and num1>num3:
    print("greatest:", num1)
elif num2>num3:
    print("greatest:",num2)
else:
    print("greatest:",num3)