from datetime import datetime


class Transaction:
    def __init__(self, amount):
        self.__time = self.__getTimeAsStr()
        self.__amount = amount

    def __getTimeAsStr(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    def getTime(self):
        return self.__time

    def getAmount(self):
        return self.__amount 

    def __str__(self):
        return f"timestamp:{self.__getTimeAsStr()}, amount:{self.__amount}" 


class Account:
    def __init__(self, custID, accountNo, balance, interest):
        self.__custID = custID
        self.__accountNo = accountNo
        self.__balance = balance
        self.__interest = interest
        self.__transactions = []

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        assert amount > 0, "Amount cant be smaller than 1"
        self.__balance += amount
        self.__transactions.append(Transaction(amount))
        return self.__balance

    def withdraw(self, amount):
        assert self.__balance >= amount, "Cant withdraw more than is in the account"
        self.__balance -= amount
        self.__transactions.append(Transaction(-amount))
        return self.__balance

    def showTransactions(self):
        for trans in self.__transactions:
            print(f"Transaction {trans}")

    def __str__(self):
        return f'Customer id  = {self.__custID}\nAccount no = {self.__accountNo}\nBalance = {self.__balance}\nInterest = {self.__interest}\n'

account1 = Account(1, 1000, 50000, 7)
print(account1)
account1.deposit(500)
print(f'New balance after depositing 500 is {account1.getBalance()}')
account1.withdraw(1000)
print(f'New balance after withdrawal of 10000 is {account1.getBalance()}')
account1.showTransactions()