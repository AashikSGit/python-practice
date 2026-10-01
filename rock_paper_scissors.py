# modularized

from random import choice

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ("r", "p", "s")


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
        (computer_pick == "r" and user_pick == "s") or
        (computer_pick == "s" and user_pick == "p") or
            (computer_pick == "p" and user_pick == "r")):
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
