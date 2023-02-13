from blackjacklogo import logo
import random



player_cards_list = []
dealer_cards_list = []

def player_cards(size):
    global player_cards_list
    for i in range(size):
        player_cards_list.append(random.randint(1, 13)) 
    print(f"Your cards are: {player_cards_list}")
    #return player_cards

def dealer_cards(size):
    for i in range(size):
        dealer_cards_list.append(random.randint(1, 13))
    print(f"Dealers first card: {dealer_cards_list[0]}")
    #return player_cards

def get_score(card_list):
    score = 0
    for card in card_list:
        score += card
    return score

def get_winner(player_score, dealer_score):
    if ( player_score > dealer_score ) and ( player_score <= 21 ):
        print(f"Player wins! {player_score}")
    elif ( player_score < dealer_score ) and ( dealer_score <= 21 ):
        print(f"Dealer wins! {dealer_score}")
    elif player_score > dealer_score:
        print(f"Dealer wins! {dealer_score}")
    elif player_score < dealer_score:
        print(f"Player wins! {player_score}")
    else:
        print(f"It's a tie! {player_score} {dealer_score}")
    return player_score, dealer_score

def show_cards():
    print(f"Your cards are: {player_cards_list}")
    print(f"Dealer cards are: {dealer_cards_list}")

def reinitiliase_card_list():
    global player_cards_list
    global dealer_cards_list
    player_cards_list = []
    dealer_cards_list = []

def display_winner():
        player_score = get_score(player_cards_list)
        dealer_score = get_score(dealer_cards_list)
        show_cards()
        get_winner(player_score, dealer_score)

def start_game():
    continue_game = True
    play  = input(f"Do you want to play a blackjack game? (y/n) ")
    if play == "y":
        print(logo)
        player_cards(2)
        dealer_cards(2) 
        while continue_game: 
            ans = input(f"Type 'y' to get another card or type 'n' to pass: ")
            if ans == "y":
                player_cards(1)
                dealer_cards(1)        
            elif ans == "n":
                display_winner()
                continue_game = False

            if len(player_cards_list) >= 5 or len(dealer_cards_list) >= 5:
                display_winner()
                continue_game = False
        
        response = input(f"Do you want to play again? (y/n) ")
        if response == "y":
            reinitiliase_card_list()
            main()
      
    else:
        print("Thanks for visiting our platform!")


def main():
    start_game()



main()


