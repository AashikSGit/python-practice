from random import randint


def get_die_details(dice):
    for die in range(1, dice + 1):
        number = randint(1, 6)
        print(f"Die {die}: {number}")


def main():
    dice = int(input("How many dice do you want to roll: "))
    count = 0
    while True:
        ans = input("Roll the dice? (y/n): ")
        if ans.lower() == "y":
            count += 1
            get_die_details(dice)

        elif ans.lower() == "n":
            print(f"You have rolled {count} times!")
            break
        else:
            print("Invalid choice.")


main()
