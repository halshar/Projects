import random


def main():
    intro()
    while main_loop(PLAYER_NAME):
        pass
    summary(PLAYER_NAME)


def intro():
    global PLAYER_NAME
    PLAYER_NAME = ''
    print()
    print(r'Welcome to Rock, Paper and Scissor game :)')
    print()
    PLAYER_NAME = input('Enter your name: ')


def main_loop(PLAYER_NAME):
    player = get_player_input()
    computer = random.randint(1, 3)
    check_result(player, computer, PLAYER_NAME)
    return ask_play_again(PLAYER_NAME)


def get_player_input():
    while True:
        print()
        print("1)Rock \n2)Paper \n3)Scissor\n")
        player = int(input("Enter your choice: "))
        if player in (1, 2, 3) and player == int(player):
            return player
        else:
            print("Wrong choice, try again")


def check_result(player, computer, PLAYER_NAME):
    global score_player, score_computer, score_ties
    if player == computer:
        print()
        print(f"It's a TIE!, Computer also chose {NAMES[computer]}")
        score_ties += 1
    elif WHAT_BEATS_WHAT[player] == computer:
        print()
        print(f"{PLAYER_NAME} WON! {PLAYER_NAME}'s {NAMES[player]} {WIN_ACTIONS[player]} Computer's {NAMES[computer]}")
        score_player += 1
    else:
        print()
        print(f"Computer WON! Computer's {NAMES[computer]} {WIN_ACTIONS[computer]} {PLAYER_NAME}'s {NAMES[player]}")
        score_computer += 1


def ask_play_again(PLAYER_NAME):
    print()
    print(f"{PLAYER_NAME} do want to play again: y/n")
    again = input("Enter your choice: ")
    return again in ('y')


def summary(PLAYER_NAME):
    global score_player, score_computer, score_ties
    print()
    print("Thank You! for playing :)")
    print("The results are :")
    print()
    print(f"{PLAYER_NAME} Won: ", score_player)
    print("Computer Won: ", score_computer)
    print("Ties: ", score_ties)
    print()


ROCK = 1
PAPER = 2
SCISSOR = 3

NAMES = {ROCK:'Rock', PAPER:'Paper', SCISSOR:'Scissor'}
WHAT_BEATS_WHAT = {ROCK: SCISSOR, PAPER: ROCK, SCISSOR: PAPER}
WIN_ACTIONS = {ROCK: 'crushes', PAPER: 'smothers', SCISSOR: 'cuts'}

score_player = 0
score_computer = 0
score_ties = 0


main()

