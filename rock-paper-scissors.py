#rock-paper-scissors.py

import random
from enum import IntEnum


class Move(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


# Maps each move to the move(s) it beats
BEATS = {
    Move.Rock: [Move.Scissors],
    Move.Paper: [Move.Rock],
    Move.Scissors: [Move.Paper],
}


def get_player_move() -> Move:
    """Prompt the player for a move and return it as a Move."""
    options = ", ".join(f"{m.name}[{m.value}]" for m in Move)
    raw = input(f"Choose ({options}): ")
    return Move(int(raw))


def get_computer_move() -> Move:
    """Randomly pick a move for the computer."""
    return random.choice(list(Move))


def decide_winner(player: Move, computer: Move) -> str:
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    return "player" if computer in BEATS[player] else "computer"


def play_round() -> None:
    try:
        player_move = get_player_move()
    except ValueError:
        print(f"Invalid input. Enter a number between 0 and {len(Move) - 1}.\n")
        return

    computer_move = get_computer_move()
    print(f"\nYou chose {player_move.name}, computer chose {computer_move.name}.")

    result = decide_winner(player_move, computer_move)
    if result == "tie":
        print("It's a tie!\n")
    elif result == "player":
        print("You win!\n")
    else:
        print("You lose!\n")


def main() -> None:
    print("=== Rock Paper Scissors ===\n")
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()