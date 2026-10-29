
    else:
        print(f"Withdrawn {amount} successfully.Balance is {balance-amount}")
        balance-=amount
withdraw(500,1000)


def send_money(amount,balance):
    if amount > balance: