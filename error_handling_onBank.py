class Account:

    def __init__(self, acnumber, acholdername, acbalance,pin):
        self.__acnumber = acnumber
        self.__acholdername = acholdername
        self.__acbalance = acbalance
        self.__pin=pin
        
    def deposit(self):

        

        try:
            acc_pin=int(input("enter your pin!!!"))
            if self.__pin==acc_pin:
                deposit_amount = int(input("Enter the amount to deposit-->>> "))
            else:
                print("Invalid pin!! please try again")
            if deposit_amount > 0:
                self.__acbalance += deposit_amount
                print("Deposit Successful")
            else:
                print("Invalid Amount.must be greater than 0.")
        except ValueError:
            print("Error: Please enter numbers only!")
            

    def show_balance(self):
        
        
        try:
            acc_pin=int(input("enter your pin!!!"))
            if self.__pin==acc_pin:
                print("Current Balance:", self.__acbalance)
                
            else:
                print("Invalid pin!! please try again")
        except ValueError:
             print("Error:please enter number only")
                

    def withdraw(self):
       
         acc_pin=int(input("enter your pin!!!"))
         if self.__pin!=acc_pin:
                
            print("Invalid pin!! please try again")
            return
        
         try:
                 
            w_amount=int(input("enter the amount to withdraw-->>>"))
           
            if w_amount>self.__acbalance:
                print("Insufficient balance.")
            else:
                self.__acbalance-=w_amount
                print(f"from your account RS:{w_amount} withrawed successfully!")
         except ValueError:
             print("Erro:enter number only")
             
      
bharathi=Account(938426,"bharathikannan",9000,1234)


while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit | 2. Show Balance | 3. Withdraw | 4. Exit")
    choice = input("Select an option (1-4): ")

    
    match choice:
        case "1":
            bharathi.deposit()
        case "2":
            bharathi.show_balance()
        case "3":
            bharathi.withdraw()
        case "4":
            print("Thank you for using our banking services. Goodbye!")
            break  
        case _:
            print("Invalid choice! Please choose an option between 1 and 4.")

    
