import random
database = []
opt = None

#functions for welcome page.
def welcome():
        print("welcome to johntega Bank app")
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
                                     
#functions for creating a new account
def signup():
     ran = random.randint(1, 10000000000)

     newUser = {
          'fname': input("Input first Name\n"),
          'lname': input("Input last Name\n"),
          'balance': 00,'pin': int(input("enter a pin\n")),
          'account_no': int(ran)
          }

    
     database.append(newUser)
     print(f"Account with the Name: {newUser['fname']} {newUser['lname']}, with Account NO:{newUser['account_no']},Balance: N{newUser['balance']}") 
     print(database)
     return welcome()  
#functions for displaying account information   
def display():
        acct_num = int(input("Enter your account number: "))
        acct_pin = int(input("Enter your account pin: "))
        acct_correct = False
        pin_correct = False

        for acct in database:
            if acct["account_no"] == acct_num:
                acct_correct = True

            else:
                print("No customer with this Account number")

            if acct_correct == True:
                if acct["pin"] == acct_pin:
                    print(f"Account info: \n Account Name:{acct['fname']} {acct['lname']}\nAccount No:{acct['account_no']}\n Balance: N{acct['balance']}")

            else:
                print("Incorrect pin")
            return welcome() 
   
#functions for deposit into account
def deposit():
        acct_num = int(input("Input your account number:"))
        amount = int(input("Input Amount to be deposted:"))

        for acct in database:
            if acct["account_no"]== acct_num:
                acct["balance"] += amount
                print(f"The sum of N{amount} has been deposited to {acct['fname']} {acct['lname']}\nBalance: N{acct['balance']}")

            else:
                pass
            return welcome() 


#functions for transfer
def transfer():
        sender_acct_num = int(input("Input sender's account number:"))
        recivers_acct_num = int(input("Input recipient's account number:"))
        senders_pin = int(input("Input sender's pin:"))
        amount = int(input("Input amount to transfer:"))

        for acct in database:
            if acct["account_no"]==sender_acct_num:
                if acct["pin"]==senders_pin:
                    if  acct["balance"]>=amount:
                        for reacct in database:
                            if  recivers_acct_num == reacct["account_no"]:
                                print(f"Account Name:{reacct['fname']}{reacct['lname']}")
                                reciver_opt = input("do you want to proceed?(input1 to proceed,any key to cancel)")
                                if reciver_opt=="1":
                                    reacct["balance"]+=amount
                                    acct["balance"]-=amount
                                    print(f"N{amount} has been successfully transferred to {reacct['fname']}")
                                else:
                                    print("Transaction cancelled")
                                    continue  

                            else:
                                print("Insufficient funds")

                    else:
                        pass
                    return welcome() 

#function for resetting password
def reset():
        acct_num = int(input("please input your account number:\n"))
        qust_1= input("Do you remember your old password (yes/no) \n")

        for acct in database:
            if acct["account_no"] == acct_num:
                if qust_1== "yes":
                    print("yes")
                    old_pass= int(input("please enter old password\n"))
                    new_pass= int(input("please enter new password\n"))
                    if acct["pin"] == old_pass:
                        acct["pin"] = new_pass
                elif qust_1 == "no":
                    fullname = (acct["fname"] + acct["lname"]).strip().lower()
                    sliceNum = slice(2, 6)
                    result = fullname[sliceNum]   
                    hide = fullname.replace(result, "****")   
                    corrchar = False
                    while corrchar == False:
                        char=input(f"please enter the missing characters {hide} \n input 'c' to cancel\n")
                        if char == result:
                            new_pass = int(input("please enter new password\n"))
                            acct["pin"] = new_pass
                            corrchar = True
                        elif char == "c":
                            break
                        else:
                            print("wrong character")
                        print(database)
                        return welcome() 



def exit():
        print("Thank you for banking with us!!!")
        opt =0
        print(database)

welcome()


















          
  

