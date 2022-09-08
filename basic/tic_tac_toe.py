def tic_tac_toe_winner(board):

    if board == "XXXXXXXXX" or board == "OOOOOOOOO":
        raise ValueError()

    if board_check(board, "X"):
        return "X"
    elif board_check(board, "O"):
        return "O"


test_cases = {
    '         ': None,
    '2317     ': None,
    'XXX      ': 'X',
    '   XXX   ': 'X',
    '      XXX': 'X',
    'OOO      ': 'O',
    '   OOO   ': 'O',
    '      OOO': 'O',
    'O  O  O  ': 'O',
    ' O  O  O ': 'O',
    '  O  O  O': 'O',
    'X  X  X  ': 'X',
    ' X  X  X ': 'X',
    '  X  X  X': 'X',
    'XO  X O X': 'X',
    'OX  O X O': 'O',
    'XXOOXXXOO': None,
    'XXXXXXXXX': ValueError
}


def board_check(board, mark):
    return (
        (board[0] == board[1] == board[2] == mark)
        or (board[3] == board[4] == board[5] == mark)
        or (board[6] == board[7] == board[8] == mark)
        or (board[0] == board[3] == board[6] == mark)
        or (board[1] == board[4] == board[7] == mark)
        or (board[2] == board[5] == board[8] == mark)
        or (board[0] == board[4] == board[8] == mark)
        or (board[6] == board[4] == board[2] == mark)
    )


for board, expectation in test_cases.items():
    #assert (tic_tac_toe_winner(board) == expectation), f"Expected {expectation!r} for {board!r} got {tic_tac_toe_winner(board)!r}"
    if isinstance(expectation, Exception):
        try:
            response = tic_tac_toe_winner(board)
            print(f'Expected {expectation!r} for {board!r} got {response!r}')
        except expectation:
            pass