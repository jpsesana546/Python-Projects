from art import logo
import random
import os


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        print("You have 10 attempts remaining to guess the number. Make a guess: ")
        attempts = 10
    elif difficulty == 'hard':
        print("You have 5 attempts remaining to guess the number. Make a guess: ")
        attempts = 5

    random_number = random.randint(1, 100)
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess < random_number:
            print("Too low. Guess again.")
        elif guess > random_number:
            print("Too high. Guess again.")
        else:
            print(f"You got it! The answer was {guess}")
            break
        attempts -= 1
    print(f"The number was {random_number}")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
