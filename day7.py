usernames = []

def atm_func(method, username):
    amount = float(input("Enter the amount: "))
    if method == 'add':
        for cred in usernames:
            if cred["username"] == username:
                curr_balance = cred["balance"]
                cred.update({"balance":curr_balance+amount})
                print(f"Balance added Successfully. Your new balance is {cred["balance"]}")
    else:
        for cred in usernames:
            if cred["username"] == username:
                curr_balance = cred["balance"]
                if amount > curr_balance:
                    print("Insufficient balance")
                    return
                cred.update({"balance":curr_balance-amount})
                print(f"Balance withdrawn Successfully. Your new balance is {cred["balance"]}")
        

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        for cred in usernames:
            if cred["username"] == username:
                print("Username already exist. Please try a new username")
                return
        dict_cred = {"username":username, "password":password, "balance":0}
        usernames.append(dict_cred)
        print("Registration Successfull")
    if method == 'login':
        for cred in usernames:
            is_login = False
            if cred["username"] == username and cred["password"] == password:
                print("Login Successfull")
                is_login = True
                while True:
                    choice = input("Enter 1 to view balance, 2 to add balance, 3 to withdraw balance, 4 to exit: ")
                    if choice == '1':
                        for cred in usernames:
                            if cred["username"] == username:
                                print(f"Current balance = {cred["balance"]}")
                            
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