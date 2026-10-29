def deposit(amount,balance):

    if amount < 0:
        print("Please enter a valid amount")

    if amount > 0:
        print(f"Deposited {amount} to account.Balance is {balance + amount}")
        balance += amount

#deposit(1000,500)

def withdraw(amount,balance):

    if amount > balance:
        print("Insufficient funds!")
    else:
        print(f"Withdrawn {amount} successfully.Balance is {balance-amount}")
        balance-=amount
#withdraw(500,1000)


def send_money(amount,balance):
    if amount > balance:
        print("Insufficiens funds..Fuliza to send")
    else:
        print(f"{amount} successfully sent to Recipient.Balance is { balance-amount}")
        balance-=amount
#send_money(3000,67000)



def bank():
    print("="*10,"MENU","="*10)
    print("\n 1.Deposit money")
    print("\n 2.Withdraw money")
    print("\n 3.Send money")
    print("\n 4.Exit")
    print("="*27)

    choice=int(input("Choose an option:"))
    if choice==1:
        deposit(500,500)
    elif choice==2:
        withdraw(400,300)
    elif choice==3:
        send_money(300,300)
    else:
        exit()


    

bank()


