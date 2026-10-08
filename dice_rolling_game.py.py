from random import randint


def get_die_details(dise):
    for die in range(1, dise + 1):
        number = randint(1, 6)
        print(f"Die {die}: {number}")


def main():
    dise = int(input("How many dise do you want to roll: "))
    count = 0
    while True:
        ans = input("Roll the dise? (y/n): ")
        if ans.lower() == "y":
            count += 1
            get_die_details(dise)

        elif ans.lower() == "n":
            print(f"You have rolled {count} times!")
            break
        else:
            print("Invalid choice.")


main()
