import random

game_start = True
game_continue = False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#
player = {}
# player[1] = random.choice(cards)
# player[2] = random.choice(cards)
# player_total = player[1]+player[2]
#
computer = {}
# computer[1] = random.choice(cards)
# computer[2] = random.choice(cards)
# computer_total = computer[1]+computer[2]

key = 0
while game_start:
    player[key+1] = random.choice(cards)
    computer[key+1] = random.choice(cards)
    key += 1
    next_pick = input("Type 'y' to get another card, type 'n' to pass: ").upper()
    if next_pick == "N":
        game_start = False

from art import logo
print(logo)

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").upper()
if play == "Y":
    game_start = True


while game_continue:

    print(f"    Your cards: [{player[1]}, {player[2]}], current score: {player_total}")
    print(f"    Computer's first card: {computer[1]}")
    next_card = input("Type 'y' to get another card, type 'n' to pass: ").upper()
    if next_card == "Y":
        player[3] = random.choice(cards)
        player_total += player[3]
        print(f"    Your cards: [{player[1]}, {player[2]},  {player[3]}], current score: {player_total}")
        print(f"    Computer's first card: {computer[1]}")
        computer[3] = random.choice(cards)
        computer_total += computer[3]
    else:
        game_start = False
# Your final hand: [4, 5], final score: 9
# Computer's final hand: [6, 11], final score: 17
#
# Youlose 😤
# Computer's final hand: [2, 10, 10], final score: 22'
# Opponent went over.You win 😁


# while game_start:
#     from art import logo
#     print(logo)