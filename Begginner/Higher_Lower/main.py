import art
import gamedata
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear()

    IG_1 = random.choice(gamedata.data)
    score = 0

    while True:
        IG_2 = random.choice(gamedata.data)
        while IG_1 == IG_2:
            IG_2 = random.choice(gamedata.data)

        print(art.logo)
        print("Welcome to Higher x Lower, guess which person has more followers on Instagram!\n")
        print(f"Compare A: {IG_1['name']}")
        print(art.vs)
        print(f"Against B: {IG_2['name']}")
        print("\n")
        print(f"Current Score: {score}")

        guess = input("Type 'h' for higher and 'l' for lower: ").lower()

        if IG_1['follower_count'] > IG_2['follower_count'] and guess == 'l':
            IG_1 = IG_2
            score += 1
            clear()
        elif IG_1['follower_count'] < IG_2['follower_count'] and guess == 'h':
            IG_1 = IG_2
            score += 1
            clear()
        elif IG_1['follower_count'] > IG_2['follower_count'] and guess == 'h':
            print(f"You lose. Score: {score}")
            break
        elif IG_1['follower_count'] < IG_2['follower_count'] and guess == 'l':
            print(f"You lose. Score: {score}")
            break

    if input("Do you want play again? Type 'y' or 'n': ").lower() == 'y':
        main()


if __name__ == "__main__":
    main()
