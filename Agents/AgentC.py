import random


class AgentC:
    def __init__(self, game):
        self.game = game
        self.name = "AgentC(Random Moves)"

    def find_best_move(self):
        valid_moves = [col for col in range(
            self.game.columns) if self.game.is_valid_move(col)]
        return random.choice(valid_moves) if valid_moves else -1
