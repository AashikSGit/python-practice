from random import randint


print("Please specify the number range you want to make a guess.")
minimum = int(input("Minimum value: "))
maximum = int(input("Maximum value: "))

random_num = (randint(minimum + 1, maximum - 1))
attempts = 0

for attempt in range(3):
    try:
        guess = int(input(f"\nGuess a number between ({minimum}-{maximum}): "))
        attempts += 1
        if guess < random_num:
            print("Too Low! Try higher.")
        elif guess > random_num:
            print("Too High! Try lower.")
        else:
            print("Correct!")
            print(f"You got it in {attempts} tries.")
            break
    except ValueError:
        print("Enter a valid number!")
else:
    print("\nattempts exceeded!")
    print(f"The answer is {random_num}")
