class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}.Balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds to withdraw")
        else:
            self.balance -=amount
            print(f"{amount} withdrawn successfully.Balance is {self.balance}")

    def send_money(self,amount):
        if amount > self.balance:
            print("Insufficient funds.Fuliza to top up")
        else:
            self.balance-=amount
            print(f"{amount} successfully sent to recipient.Balance is {self.balance}")

account1=BankAccount("Brian",3000)
account1.deposit(2000)
account1.withdraw(4000)
account1.send_money(500)
            
