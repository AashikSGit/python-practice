# modularized

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
    print(f"Computer picked {emojis[computer_pick]}")


def display_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        print("Tie! Let's try another time.")

    elif (
        (computer_pick == ROCK and user_pick == SCISSOR) or
        (computer_pick == SCISSOR and user_pick == PAPER) or
            (computer_pick == PAPER and user_pick == ROCK)):
        print("You lose!")

    else:
        print("You Won!")


def play_game():

    while True:
        computer_pick = choice(choices)
        user_pick = get_user_pick()

        display_choices(user_pick, computer_pick)

        display_result(user_pick, computer_pick)

        continue_message = input("\nContinue? (y/n): ").lower()
        if continue_message == "n":
            break


play_game()
