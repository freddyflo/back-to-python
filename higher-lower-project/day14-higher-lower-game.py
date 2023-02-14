# import required data
import random
from art import logo, vs
from game_data import data


# get index from game data
def get_random_index():
    index = random.randint(0, len(data) - 1 )
    return index

# pick data to compare from game_data
def get_data(position):
    return data[position]



def compare_followers(player_followers, computer_followers):
    if player_followers > computer_followers:
        return True
    else:
        return False

def start():

    results = True
    score = 0
    # print logo
    print(f"{logo}")
    player_index = get_random_index()
    computer_index = get_random_index()

    while results:
        if score > 0:
            print(f"Your right! Current score: {score}")

        player = get_data(player_index)
        print(f"Compare A: {player['name']}, a {player['description']}, from {player['country']}")

        # print vs logo
        print(f"{vs}")

        # get computer info
        computer = get_data(computer_index)
        print(f"Compare B: {computer['name']}, a {computer['description']}, from {computer['country']}")
        
        player_answer = input("Who has more followers? Type 'A' or 'B': ")

        # refactor
        if player_answer == "A":
            results = compare_followers(player['follower_count'], computer['follower_count'])
            score += 1
            computer_index = get_random_index()
            player_index = get_random_index()
        elif player_answer == "B":
            results = compare_followers(computer['follower_count'], player['follower_count'])
            score += 1
            player_index = computer_index
            computer_index = get_random_index()
        else:
            print(f"Unknown choice")

        print(f"Sorry, you are wrong! Game Over!")

start()