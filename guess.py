secret_number=5
max_attempts=3
while max_attempts > 0:
    try:
        guess=int(input("Guess a number to win:"))
        if guess==secret_number:
            print("Congratulations,you have won!")
            break
        else:
            print("Failed,Please try again!")
            max_attempts-=1

            if max_attempts==0:
                print("You are outof guesses")

    except ValueError:
        print("Please enter a whole number!")