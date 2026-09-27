from random import randint


random_num = (randint(1, 50))
atmp = 0

while True:
    try:
        guess = int(input("\nGuess a number between (1-50): "))
        atmp += 1
        if guess < random_num:
            print("Too Low! Try higher.")
        elif guess > random_num:
            print("Too High! Try lower.")
        else:
            print("Correct!")
            print(f"You got it in {atmp} tries.")
            break
    except ValueError:
        print("Enter a valid number!")
