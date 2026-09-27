""" Initially i had no idea that how i'd implement a rock, paper, scissors game.
still i implemented my version without any guidance. So, this would be the initial version after
i made relevant modifications"""

from random import choice

choices = {"r": "🪨", "p": "📃", "s": "✂️"}

while True:
    computer_pick = choice(["r", "p", "s"]).lower()
    user_pick = input("pick your choice (r/p/s): ").lower()

    if user_pick not in ["r", "p", "s"]:
        print("Invalid Choice!")

    elif computer_pick == "r" and user_pick == "s":
        print(f"""
Computer picked {choices[computer_pick]}
You picked {choices[user_pick]}
Computer Won!
""")

    elif computer_pick == "s" and user_pick == "p":
        print(f"""
Computer picked {choices[computer_pick]}
You picked {choices[user_pick]}
Computer Won!
""")

    elif computer_pick == "p" and user_pick == "r":
        print(f"""
Computer picked {choices[computer_pick]}
You picked {choices[user_pick]}
Computer Won!
""")

    elif computer_pick == user_pick:
        print("Draw! Let's try another time.")

    else:
        print(f"""
Computer picked {choices[computer_pick]}
You picked {choices[user_pick]}
You Won!
""")
