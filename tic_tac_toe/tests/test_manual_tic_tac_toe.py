from src.tic_tac_toe import tic_tac_toe_winner


def test_empty_board():
    assert tic_tac_toe_winner(" " * 9) is None


def test_3x_in_a_row():
    winner = tic_tac_toe_winner("XXX O O  ")
    assert winner == "X", f"expected X, got {winner}"


def test_illegal_board_symbols():
    try:
        tic_tac_toe_winner("Ala ma kota")
        assert False, "ValueError expected"
    except ValueError:
        pass


def test_illegal_board_size():
    try:
        tic_tac_toe_winner("XXX")
        assert False, "ValueError expected"
    except ValueError:
        pass