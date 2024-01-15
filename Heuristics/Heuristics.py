
def heuristic(board):
    score = 0

    AI_PIECE = 'O'
    PLAYER_PIECE = 'X'
    EMPTY = ' '
    ROWS = len(board)
    COLS = len(board[0])

    def evaluate_window(window):
        eval_score = 0

        # AI configurations
        if window.count(AI_PIECE) == 4:
            eval_score += 1000
        elif window.count(AI_PIECE) == 3 and window.count(EMPTY) == 1:
            eval_score += 100
        elif window.count(AI_PIECE) == 2 and window.count(EMPTY) == 2:
            eval_score += 10

        # Player configurations
        if window.count(PLAYER_PIECE) == 4:
            eval_score -= 1500  # Immediate blocking weightage
        elif window.count(PLAYER_PIECE) == 3 and window.count(EMPTY) == 1:
            eval_score -= 120

        return eval_score

    # Evaluate vertical, horizontal, and diagonal placements
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = board[row][col:col+4]
            score += evaluate_window(window)

    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row+i][col] for i in range(4)]
            score += evaluate_window(window)

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row+i][col+i] for i in range(4)]
            score += evaluate_window(window)

    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row-i][col+i] for i in range(4)]
            score += evaluate_window(window)

    return score
