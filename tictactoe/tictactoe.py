"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == "X"):
                num_x += 1
            elif (board[i][j] == "O"):
                num_o += 1
    if (num_x == num_o):
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                s.add((i, j))
    return s


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    cp = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    if cp[i][j] != EMPTY:
        raise ValueError
    cp[i][j] = player(board)
    return cp


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(len(board)):
        # horizontal
        if (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        # vertical
        if (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]

    # diagonal
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)):
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    if (winner(board) == O):
        return -1
    return 0


def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        newBoard = result(board, action)
        v = max(v, minValue(newBoard))
    return v


def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        newBoard = result(board, action)
        v = min(v, maxValue(newBoard))
    return v


def maxValue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        newBoard = result(board, action)
        v = max(v, minValue(newBoard))
    return v


def minValue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        newBoard = result(board, action)
        v = min(v, maxValue(newBoard))
    return v


def minimax(board):
    if terminal(board):
        return None
    optimalMove = tuple()
    max = math.inf
    min = -math.inf
    for action in actions(board):
        # max player
        if player(board) == X:
            current = minValue(result(board, action))
            if current > min:
                min = current
                optimalMove = action
        else:
            current = maxValue(result(board, action))
            if current < max:
                optimalMove = action
                max = current
    return optimalMove


board5 = [[X, X, EMPTY],
          [EMPTY, O, O],
          [EMPTY, EMPTY, EMPTY]]

minimax(board5)
