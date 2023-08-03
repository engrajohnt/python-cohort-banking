import customer

def  service():
    print('''\n Welcome to johntegaBanking Agent service\n choose an option:
    1 = Deposit
    2 = Reset customer password
    3 = Exit''')
    Opt = input(" Enter option:")

    if Opt == "1":
        customer.deposit()
        return service()
    
    elif Opt == "2":
       customer.reset() 
       return service()

    elif Opt == "3":
         customer.exit()

    else:
        print("unkown option")
        service()  

