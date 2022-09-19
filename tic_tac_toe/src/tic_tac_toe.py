from functools import wraps

ALLOWED_SYMBOLS = "X O"


def validate_board(function):
    @wraps(function)
    def wrapper(board):
        if not len(board) == 9:
            raise ValueError("improper board size")
        if not set(board) <= set(ALLOWED_SYMBOLS):
            raise ValueError("illegal symbol")

        # walidacja pozostałych przypadków

        return function(board)

    return wrapper


@validate_board
def tic_tac_toe_winner(board):
    """
    >>> from src.tic_tac_toe import tic_tac_toe_winner
    >>> tic_tac_toe_winner('')
    Traceback (most recent call last):
        raise ValueError('improper board size')
    ValueError: improper board size
    """
    for row in range(3):
        symbols_in_row = set(board[row * 3 : (row + 1) * 3])
        if len(symbols_in_row) == 1:
            if " " not in symbols_in_row:
                return symbols_in_row.pop()
    for col in range(3):
        symbols_in_col = set(board[col::3])
        if len(symbols_in_col) == 1:
            if " " not in symbols_in_col:
                return symbols_in_col.pop()
    for diag in board[::4], board[2:-1:2]:
        symbols_on_diag = set(diag)
        if len(symbols_on_diag) == 1:
            if " " not in symbols_on_diag:
                return symbols_on_diag.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()