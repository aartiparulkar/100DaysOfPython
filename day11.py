import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)


def count_score(card_list):
    """Takes a list of cards and returns the score calculated from the cards."""
    score = sum(card_list)

    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score += sum(card_list)
    return score


def draw_card(card_list):
    """Draws a card ramdomly from the deck, updates the list of cards and score"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_list.append(random.choice(cards))
    return count_score(card_list)


def deal():
    """Distribute 2 cards at the start of the game"""
    hand = []
    draw_card(hand)
    draw_card(hand)
    return hand


def is_blackjack(card_list):
    """Returns true if there is a blackjack"""
    return len(card_list) == 2 and count_score(card_list) == 21


def play_computer_turn(hand):
    """Draws cards till score exceeds 16."""
    score = count_score(hand)
    while score <= 16:
        # Draw cards till score exceeds 16
        score = draw_card(hand)

    return score

def who_is_winner(player, computer):
    """Compares the user and computer scores"""
    player_score = count_score(player)
    computer_score = count_score(computer)

    # 2.a If computer gets blackjack. It wins ---------------------------------------
    if is_blackjack(computer):
        return "Computer has a blackjack. You lose."

    # 2.b If player gets a blackjack and computer doesn't. Player wins.
    if is_blackjack(player):
        return "You win with a blackjack!"

    if player_score > 21:
        return "Bust... You went over. You lose."

    if computer_score > 21:
        return "Computer went over. You win!"

    if player_score > computer_score:
        return "You win!"

    if computer_score > player_score:
        return "Computer wins."

    return "You tie!"


def play_game():
    print(logo)
    
    # 1. Draw 2 cards initially ------------------------------------
    computer_hand = deal()
    player_hand = deal()

    player_score = count_score(player_hand)

    while True:
        print(f"\nYour cards: {player_hand}, current score = {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if is_blackjack(player_hand) or is_blackjack(computer_hand):
            break

        if player_score > 21:
            break

        # 3. Draw a card
        hit = input("\nType 'y' to draw another card, type 'n' to pass. ")

        if hit == 'n':
            break

        draw_card(player_hand)
        player_score = count_score(player_hand)

    # 4. Player is done drawing cards. Draw cards for computer.
    computer_score = count_score(computer_hand)

    if player_score <= 21 and not is_blackjack(computer_hand):
        computer_score = play_computer_turn(computer_hand)

    result = who_is_winner(player_hand, computer_hand)

    print(f"\nYour final hand: {player_hand}, final score = {player_score}")
    print(f"Computer's final card: {computer_hand}, final score = {computer_score}")
    print(result)


while input("\nDo you want to play Blackjack? \nType 'y' to play and 'n' otherwise. ") == 'y':
    print("\n"*20)
    play_game()