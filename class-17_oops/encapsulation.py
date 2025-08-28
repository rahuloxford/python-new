class Atm:
    def __init__(self, accno, pin, balance):
        self.__accno = accno
        self.__pin = pin
        self.__balance = balance

    def deposit(self, balance):
        self.__balance += balance
        print("Deposit Successfull")
    
    def withdraw(self, balance):
        self.__balance -= balance
        print("Withdraw Successfull")

    def show_balance(self):
        print(f"Current Balance: {self.__balance}")

sbi = Atm(585746322589, 2341, 2500)
sbi.show_balance()
sbi.deposit(10000)
sbi.show_balance()
sbi.withdraw(5000)
sbi.show_balance()

# sbi.pin = 1234
# sbi.__balance = 500000

# trick to change private vars
# sbi._Atm__balance = 400000

sbi.show_balance()