'''
The game: the computer picks a secret number between 1 and 100. The player keeps guessing. After each guess, the program says “Too high” or “Too low”. When the player guesses right, the program says how many attempts it took.
'''

import random

print("Guessing Game")
best_score_hard = 10
best_score_medium = 10
best_score_easy = 10

while True:
    attempts = 1
    difficulty = input("Enter the difficulty level (easy/medium/hard): ")
    if difficulty == "easy":
        secret = random.randint(1, 10)
        possible = 10
    elif difficulty == "medium":
        secret = random.randint(1, 50)
        possible = 50
    elif difficulty == "hard":
        secret = random.randint(1, 100)
        possible = 100
    else:
        print("Invalid Choice, try again.")
        continue
    print(f"The number between {possible}!")
    for i in range(7, 0, -1):
        print(f"You Have {i} Chances!")
        guess = int(input("Guess the number: "))
        
        if guess < 1 or guess > possible:
            print(f"warning:Numbers must between 1 to {possible}! you typed {guess}!")
            continue

        elif guess > secret:
            print("Too high!",end = " ")
            if guess - 5 <= secret:
                print("You're very close!")
            else:
                print()
        elif guess < secret:
            print("Too low!",end = " ")
            if guess + 5 >= secret:
                print("You're very close!")
            else:
                print()
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            if possible == 100:
                if attempts < best_score_hard:
                    print("New Record in hard level!")
                    best_score_hard = attempts
            elif possible == 50:
                if attempts < best_score_medium:
                    print("New Record in medium level!")
                    best_score_medium = attempts
            elif possible == 10:
                if attempts < best_score_easy:
                    print("New Record in easy level!")
                    best_score_easy = attempts
            break
        if i == 1:
            print(f"Game over! The number was {secret}")
        attempts += 1
    
    next_game = (input("Do you want play again? Yes/No: ")).lower()
    if next_game == "yes" or next_game == "y":
        continue
    else:
        break
