# updated version

from random import choice

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ("r", "p", "s")

while True:
    computer_pick = choice(choices)
    user_pick = input("rock, paper or scissors? (r/p/s): ").lower()

    if user_pick not in choices:
        print("Invalid Choice!")
        continue

    print(f"You picked {emojis[user_pick]}")
    print(f"Computer picked {emojis[computer_pick]}")

    if computer_pick == user_pick:
        print("Tie! Let's try another time.")

    elif (computer_pick == "r" and user_pick == "s") or \
         (computer_pick == "s" and user_pick == "p") or \
         (computer_pick == "p" and user_pick == "r"):
        print("You lose!")

    else:
        print("You Won!")

    continue_message = input("\nContinue? (y/n): ").lower()
    if continue_message == "n":
        break
