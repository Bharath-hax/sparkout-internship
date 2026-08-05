class Account:

    def __init__(self, acnumber, acholdername, acbalance):
        self.__acnumber = acnumber
        self.__acholdername = acholdername
        self.__acbalance = acbalance

    def deposit(self):
        deposit_amount = int(input("Enter the amount to deposit: "))

        if deposit_amount > 0:
            self.__acbalance += deposit_amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    def show_balance(self):
        print("Current Balance:", self.__acbalance)

    # Getter method
    def get_balance(self):
        return self.__acbalance


class SavingsAccount(Account):

    def check_minimum_balance(self):
        if self.get_balance() >= 1000:
            print("Minimum balance maintained.")
        else:
            print("You do not have the minimum balance.")


class currentAccount(Account):
     def check_minimum_balance(self):
        if self.get_balance() >= 1000:
            print("Minimum balance maintained.")
        else:
            print("You do not have the minimum balance.")
    

acc = SavingsAccount(9384, "Bharathi", 9000)
acc=currentAccount(9384,"bharathi",900)
acc.deposit()
acc.show_balance()
acc.check_minimum_balance()
