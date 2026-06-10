#multiplication table
num =int(input("Enter a number:"))
for i in range(1,11):
    print(num, "x",i,"=",num*i)


#ficed login system with loop
credentials = []

while True:
    choice = input("\n1=Login, 2 =Register, 3=Exit")
    if choice =='1':
        username=input("Enter username:")
        print("login successful")
    elif choice == "2":
        username=input("Enter username:")
        credentials.append(username)
        print("registired successfully")
    elif choice == "3":
        print("goodbye")
    else :
        print("invalid choice")
    