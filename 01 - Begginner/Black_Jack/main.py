import random
import os
from art import logo


def deal_card():
    '''
    Deal a random card from the deck
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)


def calculated_score(user_cards):
    '''
    Take a list of user cards and adds the score
    '''

    if 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)

    if sum(user_cards) == 21 and len(user_cards) == 2:
        return 0

    return sum(user_cards)


def compare_cards(user_score, computer_score):
    '''
    Compare the user score with the computer score
    '''
    if user_score == computer_score:
        return "You tied!"
    elif computer_score == 0:
        return "You lose!"
    elif user_score == 0:
        return "You win!"
    elif user_score > 21:
        return "You lose!"
    elif computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():

    computer_cards = []
    player_cards = []

    print(logo)
    is_game_over = False

    for i in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    while is_game_over is False:

        computer_score = calculated_score(computer_cards)
        user_score = calculated_score(player_cards)

        print(f"Your hand is {player_cards}. \nCurrent score: {user_score} \n")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:

            user_should_deal = input(
                "Type 'y' for another card, type 'n' to pass: ")
            print("\n")
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculated_score(computer_cards)

    print(
        f"\nYour final hand is {player_cards}. \nFinal Score: {user_score}\n")
    print(
        f"Computer's final hand is {computer_cards}. \nFinal score: {computer_score}\n")
    print(compare_cards(user_score, computer_score)+"\n")


if __name__ == "__main__":

    while input("Do you want to play a game? Type 'y' for yes, type 'n'") == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        play_game()
