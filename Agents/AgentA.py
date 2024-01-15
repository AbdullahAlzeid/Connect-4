from Heuristics import heuristic
import random

from Heuristics import heuristic
import heapq


class AgentA:
    def __init__(self, game, depth=4):
        self.game = game
        self.depth = depth
        self.name = "AgentA(Minimax with Alpha-Beta)"
        self.pruning_counter = 0

    def minimax(self, depth, alpha, beta, maximizingPlayer, column_order):
        if depth == 0 or self.game.is_game_over():
            return heuristic(self.game.board), None

        if maximizingPlayer:
            maxEval = float('-inf')
            best_col = None
            for col in column_order:
                if self.game.is_valid_move(col):
                    self.game.make_move(col)
                    eval, _ = self.minimax(
                        depth - 1, alpha, beta, False, column_order)
                    self.game.undo_move(col)
                    if eval > maxEval:
                        maxEval = eval
                        best_col = col
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        self.pruning_counter += 1
                        break
            return maxEval, best_col

        else:
            minEval = float('inf')
            best_col = None
            for col in column_order:
                if self.game.is_valid_move(col):
                    self.game.make_move(col)
                    eval, _ = self.minimax(
                        depth - 1, alpha, beta, True, column_order)
                    self.game.undo_move(col)
                    if eval < minEval:
                        minEval = eval
                        best_col = col
                    beta = min(beta, eval)
                    if beta <= alpha:
                        self.pruning_counter += 1
                        break
            return minEval, best_col

    def get_center_priority_order(self):

        return [3, 2, 4, 1, 5, 0, 6]

    def order_moves(self):
        moves_values = {}
        for col in self.get_center_priority_order():
            if self.game.is_valid_move(col):
                self.game.make_move(col)
                eval, _ = self.minimax(
                    self.depth - 1, float('-inf'), float('inf'), False, self.get_center_priority_order())
                self.game.undo_move(col)
                moves_values[col] = eval

        sorted_columns = [col for col, value in heapq.nlargest(
            len(moves_values), moves_values.items(), key=lambda x: x[1])]
        return sorted_columns

    def find_best_move(self):
        best_move = -1
        best_value = float('-inf')

        ordered_moves = self.order_moves()

        for col in ordered_moves:
            if self.game.is_valid_move(col):
                self.game.make_move(col)
                move_value, _ = self.minimax(
                    self.depth - 1, float('-inf'), float('inf'), False, ordered_moves)
                self.game.undo_move(col)
                if move_value > best_value:
                    best_value = move_value
                    best_move = col

        return best_move
