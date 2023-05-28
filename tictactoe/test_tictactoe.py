from tictactoe import *
import pytest

X = "X"
O = "O"
EMPTY = None
boardEmpty = [[EMPTY, EMPTY, EMPTY], [
    EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
board1 = [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
board2 = [[X, EMPTY, EMPTY],
          [X, O, O],
          [EMPTY, X, EMPTY]]
board3 = [[X, EMPTY, EMPTY],
          [X, O, O],
          [O, X, EMPTY]]
board4 = [[X, EMPTY, O],
          [X, O, O],
          [EMPTY, X, EMPTY]]


boardTerminal = [[X, O, O], [X, X, O], [X, X, O]]

boardXwin = [[EMPTY, O, O],
             [X, X, X],
             [EMPTY, EMPTY, EMPTY]]
boardOwin = [[X, X, O],
             [X, O, EMPTY],
             [O, EMPTY, EMPTY]]


def test_player():
    assert player(boardEmpty) == X
    assert player(board1) == O
    assert player(board2) == O
    assert player(board3) == X


def test_actions():
    assert actions(board1) == {(0, 1), (0, 2),
                               (1, 0), (1, 1), (1, 2),
                               (2, 0), (2, 1), (2, 2)}
    assert actions(board2) == {(0, 1), (0, 2),
                               (2, 0), (2, 2)}
    assert actions(boardEmpty) == {(0, 0), (0, 1), (0, 2),
                                   (1, 0), (1, 1), (1, 2),
                                   (2, 0), (2, 1), (2, 2)}


def test_result():
    assert result(boardEmpty, (0, 0)) == [[X, EMPTY, EMPTY], [
        EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert result(board2, (0, 2)) == [
        [X, EMPTY, O], [X, O, O], [EMPTY, X, EMPTY]]


def test_result_raises():
    with pytest.raises(ValueError):
        result(board2, (0, 0))


def test_winner():
    assert winner(boardOwin) == O
    assert winner(boardXwin) == X


def test_terminal():
    assert terminal(boardOwin) == True
    assert terminal(boardXwin) == True
    assert terminal(boardTerminal) == True
    assert terminal(boardEmpty) == False
    assert terminal(board1) == False
    assert terminal(board2) == False


def test_utility():
    assert utility(boardOwin) == -1
    assert utility(boardXwin) == 1
    assert utility(board1) == 0


oShouldBlockX = [[X, X, EMPTY],
                 [X, O, EMPTY],
                 [O, O, X]]

board5 = [[X, X, EMPTY],
          [EMPTY, O, O],
          [EMPTY, EMPTY, EMPTY]]


def test_minimax():

    assert minimax(oShouldBlockX) == (0, 2)
    assert minimax(board4) == (2, 0)
    assert minimax(board5) == (0, 2)
