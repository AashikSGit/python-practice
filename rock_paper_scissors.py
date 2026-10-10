# Included a competetive aspect, so that the winner will be declared based on Highscore.

from random import choice

ROCK = "r"
PAPER = "p"
SCISSOR = "s"
emojis = {ROCK: "🪨", PAPER: "📃", SCISSOR: "✂️"}
choices = tuple(emojis.keys())


def get_user_pick():
    while True:
        user_pick = input("rock, paper or scissors? (r/p/s): ").lower()

        if user_pick in choices:
            return user_pick
        else:
            print("Invalid Choice!")


def display_choices(user_pick, computer_pick):
    print(f"You picked {emojis[user_pick]}")
    print(f"Bot picked {emojis[computer_pick]}")


def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return ("Tie!\n")

    elif (
        (computer_pick == ROCK and user_pick == SCISSOR) or
        (computer_pick == SCISSOR and user_pick == PAPER) or
            (computer_pick == PAPER and user_pick == ROCK)):
        return ("Bot won\n")

    else:
        return ("You Won!\n")


def get_score(result, user_score, computer_score):
    if result == "You Won!\n":
        user_score += 1
    elif result == "Bot won\n":
        computer_score += 1

    return user_score, computer_score


def main():
    # This scope contains the game module and uses some sub-functions.
    computer_pick = choice(choices)
    user_pick = get_user_pick()

    display_choices(user_pick, computer_pick)
    print("------------")

    main_result = get_result(user_pick, computer_pick)
    print(main_result)

    return main_result


def play_game():
    # This scope executes the game module and determines winner.

    print("""
Welcome to RPS game!
The game Gives you 3 attempts to play with the RPS bot.
The winner will be determined based on the high score.
""")
    user_score = computer_score = 0

    for chance in range(3):
        result = main()

        user_score, computer_score = get_score(
            result, user_score, computer_score)

    if user_score == computer_score:
        print("Game Draw!")

    elif user_score > computer_score:
        print("Winner: You")

    else:
        print("Winner: Bot")


if __name__ == "__main__":
    play_game()
