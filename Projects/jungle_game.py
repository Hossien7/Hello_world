import random
from tabulate import tabulate


def choose_animal(animals):
    rand = random.randint(1,(len(animals) - 1))
    return rand


def score_board(data):
    print(tabulate(data, headers='keys', tablefmt='grid', numalign='center'))


def main():
        
    animals = ['elephant', 'mouse', 'cat', 'lion']
    user = input("Enter the name of your selection: ")
    players = [
        {'player1 (cpu)': animals[choose_animal(animals)], 'score': 0},
        {'player2 (cpu)': animals[choose_animal(animals)], 'score': 0},
        {'player3': user, 'score': 0}
    ]
    

    score_board(players)

if __name__ == '__main__':
    main()

