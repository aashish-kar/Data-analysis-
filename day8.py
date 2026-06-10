# FIle Handling

# FIle handling flow
# Open the file => open(file_path, opening_mode)
# opening mode => r, w, a
# Operation perform
# close the file

# If file is opened in read mode, and the file doesnot exist
# It gives an error
# file = open("abc.txt", 'r')
# content = file.read()
# file.close()
# print(content)

# file = open("abc2.txt","w")
# We can only write string or JSON in file
# IF file is opened in write mode but file doesnot exist,
# It creates a new file
# if a file is opened in write mode and we write certain content,
# it erases the previous content and only writes the new content
# file.write("hi")
# file.close()

# file = open("abc3.txt","a")
# # IF file is opened in append mode but file doesnot exist,
# # It creates a new file
# # if a file is opened in append mode and we write certain content,
# # it preserves the previous content and appends the new content at last
# file.write(" I am a data scientist ")
# file.close()



import json
# json.dumps() => Converts dictionary to json
# json.loads() => converts json to doctionary


def atm_func(method, username):
    amount = float(input("Enter the amount: "))
    backup = ""
    if method == 'add':
        file = open("credentials.txt","r")
        content = file.read()
        file.close()
        
        list_cred = content.split("-")
        for cred in list_cred:
            if cred != "":
                dict_cred = json.loads(cred)
                if dict_cred["username"] == username:
                    curr_balance = dict_cred["balance"]
                    new_balance = curr_balance + amount
                    dict_cred.update({"balance":new_balance})
                    backup += json.dumps(dict_cred)+"-"
                else:
                    backup += json.dumps(dict_cred)+"-"
        file = open("credentials.txt","w")
        file.write(backup)
        file.close()
        
    else:
        file = open("credentials.txt","r")
        content = file.read()
        file.close()
        
        list_cred = content.split("-")
        for cred in list_cred:
            if cred != "":
                dict_cred = json.loads(cred)
                if dict_cred["username"] == username:
                    curr_balance = dict_cred["balance"]
                    if curr_balance < amount:
                        print("Insuffiecient balance")
                        return
                    new_balance = curr_balance - amount
                    dict_cred.update({"balance":new_balance})
                    backup += json.dumps(dict_cred)+"-"
                else:
                    backup += json.dumps(dict_cred)+"-"
        file = open("credentials.txt","w")
        file.write(backup)
        file.close()
        

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        file = open("credentials.txt","r")
        content = file.read()
        file.close()
        list_cred = content.split("-")
        for cred in list_cred:
            if cred != "":
                dict_cred = json.loads(cred)
                if dict_cred["username"] == username:
                    print("Username already exist. Please try a new username")
                    return
        
        dict_cred = {"username":username, "password":password, "balance":0}
        file = open("credentials.txt","a")
        file.write(json.dumps(dict_cred)+"-")
        file.close()
        print(f"Registration Successful for username {username}")
        
    if method == 'login':
        file = open("credentials.txt","r")
        content = file.read()
        file.close()
        
        list_cred = content.split("-")
        for cred in list_cred:
            if cred != "":
                dict_cred = json.loads(cred)
                if dict_cred["username"] == username and dict_cred["password"] == password:
                    print("Login Successful")
                    is_login = True
                    while True:
                        choice = input("Enter 1 to view balance, 2 to add balance, 3 to withdraw balance, 4 to exit: ")
                        if choice == '1':
                            file = open("credentials.txt","r")
                            content = file.read()
                            file.close()
                            list_cred = content.split("-")
                            for cred in list_cred:
                                if cred != "":
                                    dict_cred = json.loads(cred)
                                    if dict_cred["username"] == username:
                                        print(f"Current balance = {dict_cred["balance"]}")          
                        elif choice == '2':
                            atm_func('add', username)
                        elif choice == '3':
                            atm_func('withdraw', username)
                        elif choice == '4':
                            print("Exiting from ATM system")
                            break
                        else:
                            print("Invalid input")
            if not is_login:
                print("Login Failed")
        else:
            print("Invalid Credentials")
        
                
# FOR ELSE
# IF break encounters in for block, it exits the complete loop (it exits the else part also)
# Else, else part only is executed
            
        

while True:
    choice = input("Enter 1 for register, 2 for login, 3 for exit:  ")
    if choice == '1':
        operation('register')
    elif choice == '2':
        operation('login')
    elif choice == '3':
        print("Exiting")
        break
    else:
        print("Invalid input")