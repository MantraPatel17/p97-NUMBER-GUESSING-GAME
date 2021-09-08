import random

correct_Number = random.randint(1, 9)
chances = 0

print("Number Guessing Game")
print("Guess A Number Between 1 and 9")

while chances < 5:

    guess = int(input("Enter Your Guess: "))

    if guess == correct_Number:
        print("You win!!! 😁😀")
        print("Thank you for playing this game")
        break
       
    elif guess < correct_Number:
        print("Your guess was too low: Guess a number higher than ", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances = chances + 1

    if not chances < 5:
        print("You Lose 😔😔")
