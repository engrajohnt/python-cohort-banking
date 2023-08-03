
import random

database = []
opt = None






#functions for welcome page.
def welcome():
        print("welcome to Engr-johntega Bank app")
        opt= input('''\n choose an option:
               0= Exit
               1= Create Account
               2= Display Account details
               3= Deposit funds
               4= Transfer funds
               5= Reset password\n Enter option:''')  
        if opt == "1":
             signup()  
        elif opt == "2":
             display()
        elif opt == "3":
             deposit()
        elif opt == "4":
             transfer()
        elif opt == "5":
             reset()
        elif opt == "0":
             exit()
             
        else:
             print("Unknown option")
             welcome()     
def exit():
    import main
    main.apply
    

def signup():
    ran = random.randint(1, 10000000000)

    newUser = {
        'fname': input("Input first Name\n"),
        'lname': input("Input last Name\n"),
        'balance': 0,
        'pin': int(input("Enter a pin\n")),
        'account_no': int(ran)
    }

    database.append(newUser)
    print(f"Account with the Name: {newUser['fname']} {newUser['lname']}, with Account NO:{newUser['account_no']}, Balance: N{newUser['balance']}") 
    with open("database.txt", "a") as db_files:
        if len(database) == 1:
            db_files.write(str(newUser))
        else:
            db_files.write(str(f"\n{newUser}"))

    print(database)
    return welcome()

# Function for displaying account information   
def display():
    acct_num = int(input("Enter your account number: "))
    acct_pin = int(input("Enter your account pin: "))
    acct_correct = False

    with open("database.txt", "r") as db:
        data = db.readlines()
        for line in data:
            each_data = eval(line.strip())
            if each_data["account_no"] == acct_num:
                acct_correct = True
                break

        if not acct_correct:
            print("No customer with this Account number")
            return welcome()

        if each_data["pin"] == acct_pin:
            print(f"Account info: \n{each_data}")
        else:
            print("Incorrect pin")
        
    return welcome()

def deposit():
    acct_num = int(input("Enter your account number: "))
    acct_pin = int(input("Enter your account pin: "))
    acct_correct = False

    with open("database.txt", "r") as db:
        data = db.readlines()
        for line in data:
            each_data = eval(line.strip())
            if each_data["account_no"] == acct_num:
                acct_correct = True
                break

        if not acct_correct:
            print("No customer with this Account number")
            return welcome()

        if each_data["pin"] == acct_pin:
            amount = float(input("Enter the amount to deposit: "))
            each_data["balance"] += amount
            with open("database.txt", "w") as db:
                for user_data in database:
                    if user_data["account_no"] == each_data["account_no"]:
                        db.write(str(each_data) + "\n")
                    else:
                        db.write(str(user_data) + "\n")
            print(f"Deposit successful. New balance: N{each_data['balance']}")
        else:
            print("Incorrect pin")
        
    return welcome()

def transfer():
    sender_acct_num = int(input("Enter your account number: "))
    sender_acct_pin = int(input("Enter your account pin: "))
    receiver_acct_num = int(input("Enter the recipient's account number: "))
    amount = float(input("Enter the amount to transfer: "))

    sender_found = False
    receiver_found = False

    with open("database.txt", "r") as db:
        data = db.readlines()
        for line in data:
            each_data = eval(line.strip())
            if each_data["account_no"] == sender_acct_num:
                if each_data["pin"] == sender_acct_pin:
                    if amount <= each_data["balance"]:
                        sender_found = True
                        each_data["balance"] -= amount
                    else:
                        print("Insufficient balance.")
                        return welcome()
                else:
                    print("Incorrect pin for the sender's account.")
                    return welcome()
            
            if each_data["account_no"] == receiver_acct_num:
                receiver_found = True
                each_data["balance"] += amount

    if not sender_found:
        print("Sender's account not found.")
    elif not receiver_found:
        print("Receiver's account not found.")
    else:
        with open("database.txt", "w") as db:
            for user_data in database:
                db.write(str(user_data) + "\n")
        print("Transfer successful.")

    return welcome()

def reset():
    acct_num = int(input("Enter your account number: "))
    new_pin = int(input("Enter your new pin: "))
    acct_found = False

    with open("database.txt", "r") as db:
        data = db.readlines()
        for line in data:
            each_data = eval(line.strip())
            if each_data["account_no"] == acct_num:
                acct_found = True
                each_data["pin"] = new_pin

    if not acct_found:
        print("No customer with this Account number")
    else:
        with open("database.txt", "w") as db:
            for user_data in database:
                db.write(str(user_data) + "\n")
        print("PIN reset successful.")

    return welcome()

