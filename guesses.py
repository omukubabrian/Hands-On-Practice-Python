import random
secret=random.randint(1,8)
max_attempts=4

while max_attempts > 0:
    try:
        guess=int(input("Guess a number to win:"))
        if guess==secret:
            print("Congratulations!You have won")
            break
        else:
            print("Sorry!You failed")
            max_attempts -=1
            if max_attempts==0:
                print("You are out of guesses")
    except ValueError:
        print("Please enter a whole number")

        

