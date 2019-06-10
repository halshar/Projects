import random


def intro():
    print()
    print('Welcome to Guess the Number :)')
    player_name = input('Enter your name: ')
    game_range(player_name)


def game_range(player_name):
    ans = True
    while ans:
        print()
        n = input('Enter the range of the guess i.e 10, 100, etc: ')
        if n.isdigit():
            n = int(n)
            computer = random.randint(1, n)
            take_player_input(n, computer, player_name)
            break
        else:
            print('Wrong input :( the range should be an integer, try again')
            continue


def take_player_input(n, computer, player_name):
    ans = False
    while not ans:
        print()
        player = input('Guess the number: ')
        if player.isdigit():
            player = int(player)
            check_result(player, computer, player_name, n)
            break
        elif player.isdigit() and int(player) not in range(1, n):
            print('Wrong input :( the number should be from your given range, try again')
        else:
            print('Wrong input :( the number should be an integer, try again')
            continue


def check_result(player, computer, player_name, n):
    if player == computer:
        print(f'{player_name} WON! The correct answer is {computer}')
        summary()

    elif player > computer:
        print('Too high :(, try again')
        take_player_input(n, computer, player_name)

    else:
        print('Too low :(, try again')
        take_player_input(n, computer, player_name)


def summary():
    print()
    print('Thank You! for playing Guess the Number :)')
    print()


intro()
