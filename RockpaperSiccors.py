import random
options=["rock","paper","scissors"]
computer_choice=random.choice(options)
user_choice= input("Guess either Rock,paper or scissors:").strip().lower()

while True:
    if user_choice not in options:
        print("Ensure you type correctly")
        break
    elif computer_choice==user_choice:
        print("Wow!You tied!")
        break

    elif (user_choice=="paper" and computer_choice=="rock" ) or (user_choice=="scisssors" and computer_choice=="paper") or (user_choice=="rock" and computer_choice=="scissors"):
        print("Congratulations!You win!")
        break
    else:
        print("You lose!Try again")
        break

    

