#multiplication table
num =int(input("Enter a number:"))
for i in range(1,11):
    print(num, "x",i,"=",num*i)


#ficed login system with loop
credentials =[]

while True:
    choice = input("\n1=Login,2=Register,3=Exit:")
    if choice =='1':
        username =input("Enter username:")
        if username in credentials:
            print("Login successful")
        else:
            print("Login failed")
    elif choice =='2':
        username = input("Enter username")
        credentials.append(username)
        print("Registered successfully")
    elif choice == '3':
        print("Goodbye")
        break
    else:
        print("Invalid choice")