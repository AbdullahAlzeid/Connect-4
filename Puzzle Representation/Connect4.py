class Connect4:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 'X'
        self.move_count = 0

    def is_valid_move(self, column):
        return self.board[0][column] == ' '

    def is_game_over(self):
        # Check for horizontal wins
        for row in self.board:
            for j in range(self.columns - 3):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] and row[j] != ' ':
                    return True

        # Check for vertical wins
        for j in range(self.columns):
            for i in range(self.rows - 3):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] and self.board[i][j] != ' ':
                    return True

        # Check for diagonal (top-left to bottom-right) wins
        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] and self.board[i][j] != ' ':
                    return True

        # Check for diagonal (top-right to bottom-left) wins
        for i in range(self.rows - 3):
            for j in range(3, self.columns):
                if self.board[i][j] == self.board[i + 1][j - 1] == self.board[i + 2][j - 2] == self.board[i + 3][j - 3] and self.board[i][j] != ' ':
                    return True

        # Check for a draw (if board is full)
        for col in self.board[0]:
            if col == ' ':
                return False

        return True

    def undo_move(self, column):
        for i in range(self.rows):
            if self.board[i][column] != ' ':
                self.board[i][column] = ' '
                break
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def display_board(self):
        print("\n")
        for row in self.board:
            print("|".join(row))
            print("-" * (2 * self.columns - 1))
        print("\n")

    def make_move(self, column):
        if not self.is_valid_move(column):
            return False
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.current_player
                break
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.move_count += 1  # <-- Increment the move count here
        return True

    def get_move_count(self):
        """Return the number of moves made in the game."""
        return self.move_count

    def reset(self):
        self.board = [[' ' for _ in range(self.columns)]
                      for _ in range(self.rows)]

        self.current_player = 'X'
        self.move_count = 0
