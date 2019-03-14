import unittest

from noughts_and_crosses import make_move, is_winning_line, create_line_value_lists, resolve_lines_to_check, \
    toggle_player, calculate_available_moves


class TestNoughtsAndCrosses(unittest.TestCase):

    def test_make_move(self):
        board = {
            1: None,
            2: None
        }
        position_picked = '1'
        player_character = 'X'
        updated_board = make_move(board, position_picked, player_character)
        self.assertEqual(updated_board[1], 'X')
        self.assertEqual(updated_board[2], None)

    def test_is_winning_line(self):
        line = ['X', 'X', 'X']
        win = is_winning_line(line)
        self.assertTrue(win)

    def test_is_winning_line_partially_filled(self):
        line = ['X', 'X', None]
        win = is_winning_line(line)
        self.assertFalse(win)

    def test_is_winning_line_empty_line(self):
        line = [None, None, None]
        win = is_winning_line(line)
        self.assertFalse(win)

    def test_is_winning_line_mixed_line(self):
        line = ['X', 'O', 'X']
        win = is_winning_line(line)
        self.assertFalse(win)

    def test_resolve_lines_to_check_position_1(self):
        position_picked = 1
        lines_to_check = resolve_lines_to_check(position_picked)
        self.assertEqual([[1, 2, 3], [1, 4, 7], [1, 5, 9]], lines_to_check)

    def test_resolve_lines_to_check_position_5(self):
        position_picked = 5
        lines_to_check = resolve_lines_to_check(position_picked)
        self.assertEqual([[4, 5, 6], [2, 5, 8], [1, 5, 9], [3, 5, 7]], lines_to_check)

    def test_create_line_value_lists(self):
        lines_to_check = [[1, 2, 3], [1, 4, 7], [1, 5, 9]]
        board = {
            1: 'X',
            2: 'X',
            3: 'X',
            4: 'O',
            5: 'O',
            6: 'O',
            7: 'X',
            8: 'O',
            9: 'X'
        }
        line_value_lists = create_line_value_lists(board, lines_to_check)
        self.assertEqual([['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']], line_value_lists)

    def test_toggle_player(self):
        current_player = 1
        player = toggle_player(current_player)
        self.assertEqual(0, player)
        current_player = 0
        player = toggle_player(current_player)
        self.assertEqual(1, player)

    def test_calculate_available_moves_empty_board(self):
        board = {
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
        available_moves = calculate_available_moves(board)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], available_moves)

    def test_calculate_available_moves_partially_filled_board(self):
        board = {
            1: None,
            2: 'X',
            3: 'X',
            4: None,
            5: None,
            6: 'O',
            7: 'X',
            8: None,
            9: None
            }
        available_moves = calculate_available_moves(board)
        self.assertEqual([1, 4, 5, 8, 9], available_moves)

    def test_calculate_available_moves_filled_board(self):
        board = {
            1: 'X',
            2: 'X',
            3: 'X',
            4: 'O',
            5: 'O',
            6: 'O',
            7: 'X',
            8: 'X',
            9: 'O'
            }
        available_moves = calculate_available_moves(board)
        self.assertEqual([], available_moves)
