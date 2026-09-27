from random import randint


while True:
    ans = input("Roll the dise? (y/n): ")
    if ans.lower() == "y":
        die_1 = randint(1, 6)
        die_2 = randint(1, 6)
        print(f"({die_1}, {die_2})")

    elif ans.lower() == "n":
        print("Have a nice day!")
        break
    else:
        print("Invalid choice.")
