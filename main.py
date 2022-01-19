import random
import pandas as pd

winning_combinations = [['a1', 'a2', 'a3'],
                        ['b1', 'b2', 'b3'],
                        ['c1', 'c2', 'c3'],
                        ['a1', 'b1', 'c1'],
                        ['a2', 'b2', 'c2'],
                        ['a3', 'b3', 'c3'],
                        ['a1', 'b2', 'c3'],
                        ['c1', 'b2', 'a3']]


def start_message():
    print('+-+-+-+-+-+-+-+-+-+-+-+\n'
          '|T|i|c|-|T|a|c|-|T|o|e|\n'
          '+-+-+-+-+-+-+-+-+-+-+-+\n')
    print('Would you like to play a game of Tic-Tac-Toe? y/n:')
    answer = input().lower()

    if answer == 'y':
        start_game()
    elif answer == 'n':
        print('Good_bye')
        exit()
    else:
        print('Sorry i didn´t understand that.\n'
              "Please answer 'y' or 'n'")
        start_message()


def ai_turn(data):
    free_squares = data[data == ' '].stack().index.tolist()
    ai_letter, ai_number = random.choice(free_squares)
    data[ai_number][ai_letter] = 'o'


def check_score(data):
    for combination in winning_combinations:
        first = data[combination[0][1]][combination[0][0]]
        second = data[combination[1][1]][combination[1][0]]
        third = data[combination[2][1]][combination[2][0]]

        if first == second == third:
            winner = first
            if winner == 'x':
                show_board(data)
                print('GAME OVER, YOU WIN!')
                start_message()
            elif winner == 'o':
                show_board(data)
                print('GAME OVER, YOU LOSE!')
                start_message()
            else:
                pass


def count_score(player_count, ai_count):
    if player_count.count() == 3:
        print('game over function, win')
    elif ai_count.count() == 3:
        print('game over function, loss')
    else:
        pass


def show_board(data):
    print(
        '    1     2     3  \n'
        f'a   {data["1"]["a"]}  |  {data["2"]["a"]}  |  {data["3"]["a"]}  \n'
        '  _____|_____|_____\n'
        # '     |     |     \n'
        f'b   {data["1"]["b"]}  |  {data["2"]["b"]}  |  {data["3"]["b"]}  \n'
        '  _____|_____|_____\n'
        f'c   {data["1"]["c"]}  |  {data["2"]["c"]}  |  {data["3"]["c"]}  \n'
        '       |     |     \n')


def start_game():
    df = {'a': [' ', ' ', ' '],
          'b': [' ', ' ', ' '],
          'c': [' ', ' ', ' ']}
    data = pd.DataFrame.from_dict(df, orient='index', columns=['1', '2', '3'])
    turn_counter = 0

    while True:
        show_board(data)

        player_choice = input('Enter a square, ex a1:\n') + '  '
        letter = player_choice[0]
        number = player_choice[1]

        if letter in data.index and number in data.columns:
            if data[number][letter] == ' ':
                data[number][letter] = 'x'
                turn_counter += 1
                check_score(data)

                if turn_counter < 10:
                    ai_turn(data)
                    turn_counter += 1
                    check_score(data)
                else:
                    show_board(data)
                    print('GAME OVER, DRAW!')
                    start_message()

            else:
                print('That is not a valid target')
        else:
            print('That is not a valid target')


start_message()
