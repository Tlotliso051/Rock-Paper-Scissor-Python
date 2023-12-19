import random
import math


def user_input(command):
    """
    Get user input for Rock, Paper, Scissors game.

    Parameters:
    command (str): The message displayed to the user.

    Returns:
    str: User input ('r', 's', or 'p').
    """
    while True:
        user_input = input(command).lower()
        if user_input.isalpha() and user_input in ['r', 's', 'p']:
            return user_input
        else:
            print("Enter only 'r', 's' or 'p'.")


def winner_or_loser(player, computer):
    """
    Determine the winner or loser of a Rock, Paper, Scissors game.

    Parameters:
    player (str): User's choice ('r', 's', or 'p').
    computer (str): Computer's choice ('r', 's', or 'p').

    Returns:
    tuple: A tuple containing the result code (0 for tie, 1 for player win, -1 for player loss),
           player's choice, and computer's choice.
    """
    if player == computer:
        return 0, player, computer
    
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
        return 1, player, computer
    else:
        return -1, player, computer


def display_win_or_lose(player_score, cpu_score, win_score):
    """
    Display the winner or loser of the Rock, Paper, Scissors game.

    Parameters:
    player_score (int): Number of games won by the player.
    cpu_score (int): Number of games won by the computer.
    win_score (int): Winning score threshold.

    Prints the game outcome.
    """
    if player_score > cpu_score:
        print(f"You have won {player_score} of {win_score} Games.")
    else:
        print(f"You have lost {player_score} of {win_score} Games.")


def game_function(number_of_games):
    """
    Run the Rock, Paper, Scissors game.

    Parameters:
    number_of_games (int): Number of games to play.
    player (str): user's choice (s,r or p)

    Plays the game and displays the overall outcome.
    """
    player_score, cpu_score = 0, 0
    win_score = math.ceil(number_of_games / 2)

    while player_score < win_score and cpu_score < win_score:
        player = user_input("Enter 'r' for Rock, 's' for Scissors, and 'p' for Paper: ")
        computer = random.choice(['r', 's', 'p'])
        game, player, computer = winner_or_loser(player, computer)
    

        if game == 0:
            print(f"It's a Tie. You chose {player} and computer chose {computer}.")
        elif game == 1:
            player_score += 1
            print(f"You chose {player} and computer chose {computer}. You win.")
        else:
            cpu_score += 1
            print(f"You chose {player} and computer chose {computer}. You lose.")
        print("\n")
    display_win_or_lose(player_score, cpu_score, win_score)


if __name__ == "__main__":
    game_function(3)
