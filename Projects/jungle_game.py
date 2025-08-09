import random
from tabulate import tabulate


def score_board(data):
    print(tabulate(data, headers='keys', tablefmt='grid', numalign='center'))


def if_p(player, computer):

    player_score = 0
    computer_score = 0
    # Check if player and computer selections are valid
    if player == computer:
        return 0
    
    # elephant vs others
    elif player == 'elephant' and computer == 'mouse':
        computer_score += 1
        return player_score, computer_score
    elif player == 'elephant' and computer == 'cat':
        player_score += 1
        return player_score, computer_score
    elif player == 'elephant' and computer == 'lion':
        player_score += 1
        return player_score, computer_score
    elif player == 'elephant' and computer == 'dog':
        player_score += 1
        return player_score, computer_score
    
    # mouse vs others
    elif player == 'mouse' and computer == 'cat':
        computer_score += 1
        return player_score, computer_score
    elif player == 'mouse' and computer == 'lion':
        computer_score += 1
        return player_score, computer_score
    elif player == 'mouse' and computer == 'elephant':
        player_score += 1
        return player_score, computer_score
    elif player == 'mouse' and computer == 'dog':
        computer_score += 1
        return player_score, computer_score
    
    # dog vs others
    elif player == 'dog' and computer == 'elephant':
        computer_score += 1
        return player_score, computer_score
    elif player == 'dog' and computer == 'lion':
        computer_score += 1
        return player_score, computer_score
    elif player == 'dog' and computer == 'cat':
        player_score += 1
        return player_score, computer_score
    elif player == 'dog' and computer == 'mouse':
        computer_score += 1
        return player_score, computer_score
    
    # lion vs others
    elif player == 'lion' and computer == 'elephant':
        computer_score += 1
        return player_score, computer_score
    elif player == 'lion' and computer == 'dog':
        player_score += 1
        return player_score, computer_score
    elif player == 'lion' and computer == 'cat':
        player_score += 1
        return player_score, computer_score
    elif player == 'lion' and computer == 'mouse':
        player_score += 1
        return player_score, computer_score
    
    # cat vs others
    elif player == 'cat' and computer == 'elephant':
        computer_score += 1
        return player_score, computer_score
    elif player == 'cat' and computer == 'lion':
        computer_score += 1
        return player_score, computer_score
    elif player == 'cat' and computer == 'mouse':
        player_score += 1
        return player_score, computer_score
    elif player == 'cat' and computer == 'dog':
        computer_score += 1
        return player_score, computer_score

def main():
            
    animals = ['elephant', 'mouse', 'dog', 'cat', 'lion']
    try:
        user = input("Enter the name of your selection: ")
    except ValueError:
        print("Invalid input. Please enter a valid name.")
    players = [
        {'player1 (cpu)': random.choice(animals), 'score': 0},
        {'player2 (cpu)': random.choice(animals), 'score': 0},
        {'player3': user, 'score': 0},
    ]
    score_board(players)
    print("Welcome to the Jungle Game!")

    players[2]['score'], players[0]['score'] = if_p(user, players[0]['player1 (cpu)'])
    print(players[0]['score'], players[2]['score'])
    print(players[0]['score'])
    score_board(players)

if __name__ == '__main__':
    main()
