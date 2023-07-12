database = []
opt = None



def  service():
    print('''\n Welcome to johntegaBamking Agent service\n choose an option:
    1 = Deposit
    2 = Reset customer password
    3 = Exit''')
    Opt = input(" Enter option:")

    if Opt == "1":
        from customer import deposit
        print (database)
        return service()
    
    elif Opt == "2":
       from customer import reset
       
       return service()

    elif Opt == "3":
        print("Thank you for banking with us.")
        from customer import exit

    else:
        print("unkown option")
        service()  

service()