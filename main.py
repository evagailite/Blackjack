import art
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = True
get_another_card = True


def deal_cards():
    return random.choice(cards)


def player_results(player_cards, player_score):
    print(f"Your cards: {player_cards}, current score: {player_score}")


def computer_results(computers_card):
    print(f"Computer's first card: {computers_card}")


def summary_of_cards(player_cards):
    return sum(player_cards)


while start_game:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_choice == "y":

        get_another_card = True
        clear()
        print(art.logo)

        player_cards = []
        player_cards = random.sample(cards, 2)

        player_score = summary_of_cards(player_cards)
        player_results(player_cards, player_score)

        computers_card = deal_cards()

        computer_results(computers_card)

        while get_another_card:
            user_choice2 = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice2 == "y":

                house_deal = random.choice(cards)

                if house_deal == 11 and summary_of_cards(player_cards) > 10:
                    house_deal = 1

                player_cards.insert(len(player_cards), house_deal)
                player_score = summary_of_cards(player_cards)
                player_results(player_cards, player_score)
                print(f"Computer's first card: {computers_card}")

                if player_score > 21:
                    print("You went over. You lose")
                    get_another_card = False

            elif user_choice2 == 'n':

                computer_table = []
                computer_table.append(computers_card)

                while summary_of_cards(computer_table) < 17:
                    house_deal = random.choice(cards)

                    if house_deal == 11 and summary_of_cards(computer_table) > 10:
                        house_deal = 1

                    computer_table.append(house_deal)

                computers_score = summary_of_cards(computer_table)

                print(f"Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_table}, final score: {computers_score}")

                if player_score == computers_score:
                    print("Draw!!!")
                elif player_score == 21 and len(player_cards) == 2:
                    print("Blackjack!!! You win!")
                elif computers_score == 21 and len(computer_table):
                    print("Blackjack!!! Computer win!")
                elif computers_score > 21:
                    print("Opponent went over. You win!")
                elif player_score > computers_score:
                    print("You win!")
                else:
                    print("You lose!")

                get_another_card = False

            else:
                print("Invalid input! Please try again!")

    elif user_choice == 'n':
        start_game = False
    else:
        print("Invalid input! Please try again!\n")

print("Game ends. Thank you for playing.")
