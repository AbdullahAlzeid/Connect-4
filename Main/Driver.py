from Connect4 import Connect4
from AgentA import AgentA
from AgentB import AgentB
from AgentC import AgentC
import statistics


def main():

    game = Connect4()

    # Game 1
    # agent1 = AgentA(game)
    # agent1.name = "AgentA1(Minimax with Alpha-Beta)"
    # agent2 = AgentA(game)
    # agent2.name = "AgentA2(Minimax with Alpha-Beta)"

    # Game 2
    # agent1 = AgentB(game)  # with probability 0.5
    # agent2 = AgentA(game)

    # Game 3
    # agent1 = AgentC(game)
    # agent2 = AgentA(game)

    # Game 4
    # agent1 = AgentC(game)
    # agent2 = AgentB(game)  # with probability 0.75

    # Game 5
    # agent1 = AgentC(game)
    # agent2 = AgentB(game)  # with probability 0.5

    # Game 6
    agent1 = AgentC(game)
    agent2 = AgentB(game)  # with probability 0.25

    simulate_game(agent1, agent2, 10)

    # This Block of code is for playing games between human and agent if you want to test individual agents by playing against them (I used when I was developing the agents to ensure they were working properly)

    # Board = Connect4()
    # agent = AgentA(Board)
    # while True:
    #     Board.display_board()

    #     if Board.current_player == 'X':
    #         column = int(input(
    #             f"Player {Board.current_player}'s turn. Enter column (0-{Board.columns-1}): "))

    #         if 0 <= column < Board.columns:
    #             if not Board.is_valid_move(column):
    #                 print("Invalid move. Column is full.")
    #                 continue
    #             else:
    #                 Board.make_move(column)
    #         else:
    #             print(
    #                 f"Invalid input. Please enter a number between 0 and {Board.columns-1}.")
    #             continue
    #     else:  # Agent's turn
    #         print(f"{agent.name}'s turn.")
    #         column = agent.find_best_move()
    #         print(f"{agent.name} chooses column {column}")
    #         Board.make_move(column)

    #     if Board.is_game_over():
    #         Board.display_board()
    #         if Board.current_player == 'X':
    #             print(f"{agent.name} wins!")
    #         else:
    #             print(f"Player X wins!")
    #         break

    # # Ask for a rematch
    # replay = input("Do you want to play again? (yes/no): ").strip().lower()
    # if replay == 'yes':
    #     main()


def simulate_game(agent1, agent2, n):
    with open("game_log-6.txt", "w") as file:
        total_wins_agent1 = 0
        total_losses_agent1 = 0
        total_game_lengths = []
        total_alpha_beta_pruning_agent1 = []
        total_alpha_beta_pruning_agent2 = []

        for game_number in range(1, n + 1):
            game = Connect4()
            agent1.game = game
            agent2.game = game

            file.write(f"Game {game_number}\n\n")

            while not game.is_game_over():
                current_agent = agent1 if game.current_player == 'X' else agent2

                # Let the current agent decide on a move
                col = current_agent.find_best_move()

                # Write to the file about the move
                file.write(
                    f"{current_agent.name} ({game.current_player}) played in column {col}\n")

                # Make the move
                game.make_move(col)

                # Print the board
                for row in game.board:
                    file.write("|".join(row) + "\n")
                file.write("-" * (2 * game.columns - 1) + "\n\n")

            # If the game ends without a win, it's a draw. Otherwise, the player who moved last is the winner.
            if game.get_move_count() == game.rows * game.columns:
                file.write("The game ended in a draw.\n")
            else:
                # The winner is the opposite of the current player because we've already switched players after the last move
                winner_symbol = 'O' if game.current_player == 'X' else 'X'
                winner_agent_name = agent1.name if winner_symbol == 'X' else agent2.name

                if winner_symbol == 'X':
                    total_wins_agent1 += 1
                else:
                    total_losses_agent1 += 1

                file.write(f"{winner_agent_name} won the game.\n")

            # Calculate game length and pruning statistics
            game_length = game.get_move_count()
            total_game_lengths.append(game_length)

            # Get pruning statistics for both agents
            pruning_agent1 = getattr(agent1, "pruning_counter", 0)
            pruning_agent2 = getattr(agent2, "pruning_counter", 0)

            total_alpha_beta_pruning_agent1.append(pruning_agent1)
            total_alpha_beta_pruning_agent2.append(pruning_agent2)

            if game_number != n:  # If it's not the last game, print a separator.
                file.write("\n" + "="*50 + "\n\n")

        # Calculate and report statistics
        win_to_loss_ratio = total_wins_agent1 / \
            total_losses_agent1 if total_losses_agent1 != 0 else "undefined"
        min_game_length = min(total_game_lengths)
        max_game_length = max(total_game_lengths)
        avg_game_length = statistics.mean(total_game_lengths)
        std_dev_game_length = statistics.stdev(total_game_lengths) if len(
            total_game_lengths) > 1 else "undefined"

        min_pruning_agent1 = min(total_alpha_beta_pruning_agent1)
        max_pruning_agent1 = max(total_alpha_beta_pruning_agent1)
        avg_pruning_agent1 = statistics.mean(total_alpha_beta_pruning_agent1)
        std_dev_pruning_agent1 = statistics.stdev(total_alpha_beta_pruning_agent1) if len(
            total_alpha_beta_pruning_agent1) > 1 else "undefined"

        min_pruning_agent2 = min(total_alpha_beta_pruning_agent2)
        max_pruning_agent2 = max(total_alpha_beta_pruning_agent2)
        avg_pruning_agent2 = statistics.mean(total_alpha_beta_pruning_agent2)
        std_dev_pruning_agent2 = statistics.stdev(total_alpha_beta_pruning_agent2) if len(
            total_alpha_beta_pruning_agent2) > 1 else "undefined"

        file.write("\n" + "="*50 + "\n\n")
        file.write("\nGame Statistics:\n")
        file.write(
            f"Win-to-Loss Ratio for {agent1.name}: {win_to_loss_ratio}\n")
        file.write("Game Length Statistics:\n")
        file.write(f"  Min: {min_game_length}\n")
        file.write(f"  Max: {max_game_length}\n")
        file.write(f"  Average: {avg_game_length}\n")
        file.write(f"  Standard Deviation: {std_dev_game_length}\n")

        file.write(f"\nAlpha-Beta Pruning Statistics for {agent1.name}:\n")
        file.write(f"  Min: {min_pruning_agent1}\n")
        file.write(f"  Max: {max_pruning_agent1}\n")
        file.write(f"  Average: {avg_pruning_agent1}\n")
        file.write(f"  Standard Deviation: {std_dev_pruning_agent1}\n")

        file.write(f"\nAlpha-Beta Pruning Statistics for {agent2.name}:\n")
        file.write(f"  Min: {min_pruning_agent2}\n")
        file.write(f"  Max: {max_pruning_agent2}\n")
        file.write(f"  Average: {avg_pruning_agent2}\n")
        file.write(f"  Standard Deviation: {std_dev_pruning_agent2}\n")


if __name__ == "__main__":
    main()
