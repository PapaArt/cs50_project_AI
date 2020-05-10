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
    XTurn = 0
    OTurn = 0
    empty = True

    for rolls in board:
        for cells in rolls:
            if cells is not EMPTY:
                if cells is X:
                    XTurn += 1
                else:
                    OTurn += 1
                empty = False
    
    if empty is True:
        return X
    elif XTurn > OTurn:
        return O
    else:
        return X


def actions(board):
    actions = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.append([i, j])
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        return board
    
    movement = player(board)
    result = copy.deepcopy(board)
    
    if result[action[0]][action[1]] is not EMPTY:
        raise NameError('Invalid Action')
    else:
        result[action[0]][action[1]] = movement
        return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_mode = [[[0,0],[0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]], [[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]], [[0,0], [1,1], [2,2]], [[0,2], [1,1], [2,0]]]

    for win in win_mode:
        win_set = []

        for cells in win:

            win_set.append(board[cells[0]][cells[1]])

        check = all(x == win_set[0] for x in win_set)
        if check:
            if win_set[0] is X:
                return X
            elif win_set[0] is O:
                return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Tie = True

    if winner is None:
        return False
    elif winner(board) is X or winner(board) is O:
        return True
    else:
        for rolls in board:
            for cells in rolls:
                if cells is EMPTY:
                    Tie = False
                    
    return Tie
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    Turn = player(board)
    Best_move = None

    if terminal(board):
        return None

    if empty(board):
        return[1,1]

    if Turn == X:
        Best_score = -math.inf
        for a in actions(board):
            score = Max_value(result(board, a), O)
            if score > Best_score:
                Best_score = score
                Best_move = a
    elif Turn == O:
        Best_score = math.inf
        for a in actions(board):
            score = Max_value(result(board, a), X)
            if score < Best_score:
                Best_score = score
                Best_move = a
    return Best_move

def Max_value(board, Turn):
    if terminal(board):
        return utility(board)
    
    if Turn == X:
        best = -math.inf
        for a in actions(board):
            best = max(best, Max_value(result(board, a), O))
    
    elif Turn == O:
        best = math.inf
        for a in actions(board):
            best = min(best, Max_value(result(board, a), X))
    
    return best

def empty(board):
    # check if the board is empty
    holl = True
    for rolls in board:
            for cells in rolls:
                if cells is not EMPTY:
                    holl = False
    
    return holl