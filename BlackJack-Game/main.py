#BlackJack

import random

is_game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    total = sum(cards)

    if total == 21 and len(cards) ==2:
        return 0

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
        total -= 10

    return total

def compare(player_score,dealer_score):
    if player_score == dealer_score:
        return 'Draw 🙃'
    elif player_score == 0:
        return 'Win with a BlackJack 😎'
    elif dealer_score == 0:
        return 'Lose, opponent has BlackJack 😲'
    elif player_score > 21:
        return 'You went over. You lose 😢'
    elif dealer_score > 21:
        return 'Won! Dealer went over 😁'
    else:
        return 'You lose 😤'


player_cards = []
dealer_cards = []

for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not is_game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Dealer\'s first card: {dealer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        is_game_over = True
    else:
        player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if player_should_deal == 'y':
            player_cards.append(deal_card())
        else:
            is_game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

print(f"    Your final hand: {player_cards}, final score: {player_score}")
print(f"    Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
print(compare(player_score,dealer_score))
