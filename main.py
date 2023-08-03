


def apply():
    print("Welcome to Engr JohnTegaBanking service")
    print('''\n Users:
      1 = Customer
      2 = Agent
    ''')
    User = input ("Enter user : ")
    if User == "1" :
       import customer
       customer.welcome() 
    elif User == "2":
         import agent
         agent.service()
       
    else:
        print ("Contact EngrJohnTegabankingservice.org for more info.\n")
 
apply()   