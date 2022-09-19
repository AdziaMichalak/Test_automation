import unittest
import doctest
import pytest
import src.tic_tac_toe


from src.tic_tac_toe import tic_tac_toe_winner


class TestFinishedGame(unittest.TestCase):
    def test_3x_in_a_row(self):
        for i, board in enumerate(("XXXO  O O", "O  XXXO O", "O OO  XXX")):
            with self.subTest(row=i + 1):
                self.assertEqual(tic_tac_toe_winner(board), "X")

    def test_3x_in_a_column(self):
        self.assertEqual(tic_tac_toe_winner("X  XO XOO"), "X")


def test_3x_diagonally():  # pytest keep it out of class
    assert tic_tac_toe_winner("XO OX   X") == "X"

    # kolejne testy dla planszy opisujących zakończone gry


class TestUnfinishedGame(unittest.TestCase):
    def test_empty_board(self):
        self.assertIsNone(tic_tac_toe_winner(" " * 9))

    # kolejne testy dla niezakończonych gier


class TestInvalidBoard(unittest.TestCase):
    def test_illegal_symbols(self):
        with self.assertRaises(ValueError):
            tic_tac_toe_winner("    E    ")

    # kolejne testy nieprawidłowego wejścia


def test_too_large_board():
    with pytest.raises(ValueError):
        tic_tac_toe_winner("XOOOXXXXOX")


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(src.tic_tac_toe))
    return tests