import os
import random


def create_board():
    return {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None
    }


def setup_players():
    return {0: {'name': 'ONE', 'character': 'O'},
            1: {'name': 'TWO', 'character': 'X'}}


def make_move(board, position_picked, player_character):
    position_picked_int = int(position_picked)
    board[position_picked_int] = player_character
    return board


def is_winning_line(line_value_list):
    if None in line_value_list:
        return False
    else:
        return [line_value_list[0]] * len(line_value_list) == line_value_list


def create_line_value_lists(board, lines_to_check):
    line_value_lists = []
    for line in lines_to_check:
        line_value_list = []
        for position_to_check in line:
            line_value_list.append(board[position_to_check])
        line_value_lists.append(line_value_list)
    return line_value_lists


def resolve_lines_to_check(position_picked):
    position_picked_int = int(position_picked)
    row_1 = [1, 2, 3]
    row_2 = [4, 5, 6]
    row_3 = [7, 8, 9]
    col_1 = [1, 4, 7]
    col_2 = [2, 5, 8]
    col_3 = [3, 6, 9]
    diagonal_1 = [1, 5, 9]
    diagonal_2 = [3, 5, 7]
    lines_to_check = {
        1: [row_1, col_1, diagonal_1],
        2: [row_1, col_2],
        3: [row_1, col_3, diagonal_2],
        4: [row_2, col_1],
        5: [row_2, col_2, diagonal_1, diagonal_2],
        6: [row_2, col_3],
        7: [row_3, col_1, diagonal_2],
        8: [row_3, col_2],
        9: [row_3, col_3, diagonal_1]
    }
    return lines_to_check.get(position_picked_int)


def pick_random_player():
    players = [0, 1]
    return (random.choice(players))


def toggle_player(current_player):
    x = current_player
    x ^= 1
    return x


def display_title_bar():
    print("**********************************************")
    print("************ Noughts and Crosses *************")
    print("**********************************************")


def calculate_available_moves(board):
    available_moves = []
    for place, value in board.items():
        if not value:
            available_moves.append(place)
    return available_moves


def print_game_screen(board):
    os.system('clear')
    display_title_bar()
    row = ''
    for position, value in board.items():
        if value:
            row += '\033[4m' + value + '\033[0m'
        else:
            row += '\033[4m' + str(position) + '\033[0m'
        row += ' | '
        if position % 3 == 0:
            print(row[:-2])
            row = ''


if __name__ == "__main__":
    board = create_board()
    players = setup_players()
    current_player = pick_random_player()
    game_decided = False
    available_moves = calculate_available_moves(board)


    print_game_screen(board)

    while not game_decided:

        print('Pick one of the following: ' + str(available_moves))
        player_text = "PLAYER " + players[current_player]['name'] + " (" + players[current_player]['character'] + ")"
        move = input(player_text + " - pick move position: ")

        while int(move) not in available_moves:
            move = input(player_text + ": pick A VALID move position: ")

        make_move(board, move, players[current_player]['character'])

        print_game_screen(board)

        if len(available_moves) < 6:
            lines_to_check = resolve_lines_to_check(move)
            line_value_lists = create_line_value_lists(board, lines_to_check)
            for line in line_value_lists:
                if is_winning_line(line):
                    print(player_text + ' WINS!!!!')
                    game_decided = True

        available_moves = calculate_available_moves(board)

        if len(available_moves) == 0 and game_decided is False:
            print('GAME IS A DRAW!')
            game_decided = True

        current_player = toggle_player(current_player)
