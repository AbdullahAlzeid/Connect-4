from Heuristics import heuristic
import random


class AgentB:
    def __init__(self, game, depth=4, probability=0.25):
        self.game = game
        self.depth = depth
        self.probability = probability  # probability of opponent choosing the best move
        self.name = "AgentB(Expectimax with Alpha-Beta)"
        self.pruning_counter = 0

    def expectimax(self, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.game.is_game_over():
            return heuristic(self.game.board)

        if maximizingPlayer:
            maxEval = float('-inf')
            for col in range(self.game.columns):
                if self.game.is_valid_move(col):
                    self.game.make_move(col)
                    eval = self.expectimax(depth - 1, alpha, beta, False)
                    self.game.undo_move(col)
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        self.pruning_counter += 1
                        break
            return maxEval
        else:  # Expectation layer
            expected_value = 0
            move_values = []

            for col in range(self.game.columns):
                if self.game.is_valid_move(col):
                    self.game.make_move(col)
                    eval = self.expectimax(depth - 1, alpha, beta, True)
                    move_values.append(eval)
                    self.game.undo_move(col)

            best_move_val = max(move_values) if move_values else 0
            for move_val in move_values:
                if move_val == best_move_val:
                    expected_value += self.probability * move_val
                else:
                    expected_value += (1 - self.probability) / \
                        (len(move_values) - 1) * move_val

                # Pruning condition for the expectation layer
                if expected_value > beta:
                    self.pruning_counter += 1
                    return expected_value

            return expected_value

    def find_best_move(self):
        best_move = -1
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        def is_double_threat(move, player):
            self.game.make_move(move)
            threat_count = 0
            for col in range(self.game.columns):
                if self.game.is_valid_move(col):
                    self.game.make_move(col)
                    if self.game.is_game_over() and self.game.current_player == player:
                        threat_count += 1
                    self.game.undo_move(col)
            self.game.undo_move(move)
            return threat_count > 1

        # Check for immediate threats
        for col in range(self.game.columns):
            if self.game.is_valid_move(col):
                self.game.make_move(col)
                if self.game.is_game_over():
                    self.game.undo_move(col)
                    return col
                self.game.undo_move(col)

        # Check for a two-move winning setup for the agent
        for col in range(self.game.columns):
            if self.game.is_valid_move(col) and is_double_threat(col, 'O'):
                return col

        # Check for a two-move winning setup for the opponent and block it
        for col in range(self.game.columns):
            if self.game.is_valid_move(col) and is_double_threat(col, 'X'):
                return col

        # If neither of the above conditions is met, use expectimax to decide
        available_moves = [col for col in range(
            self.game.columns) if self.game.is_valid_move(col)]
        if random.random() < self.probability:
            for col in available_moves:
                self.game.make_move(col)
                move_value = self.expectimax(
                    self.depth - 1, alpha, beta, False)
                self.game.undo_move(col)
                if move_value > best_value:
                    best_value = move_value
                    best_move = col
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
        else:
            best_move = random.choice(available_moves)

        return best_move
