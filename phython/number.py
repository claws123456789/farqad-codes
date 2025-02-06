import random

def guess():
    print("welcome to the number guessing game")
    a = random.randint(1,10)
    attempts = 0

    while True:
        try:
            guess = int(input("guess a number between 1 to 10"))
            attempts += 1

            if guess < 1 or guess > 10:
                print("ente a number between 1 to 10")
                continue
            if guess < a:
                print("too low try again")
            elif guess > a:
                print("to high try again")
            else:
               print(f" Congratulations! You guessed it in {attempts} attempts! ")
        except ValueError:
            print(" Invalid input! Please enter a number.")

guess()

