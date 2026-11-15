from currency import exchange_rates


def display_currencies():
    print("Welcome To currency converter")
    print("Supported Currencies")

    for currency in exchange_rates.keys():
        print(f"- {currency}")


def convert_currency(source_value, source_currency, target_currency):
    base_value = source_value / exchange_rates[source_currency]
    target_value = base_value * exchange_rates[target_currency]

    return target_value


def main():

    display_currencies()

    try:
        source_value = float(input("Enter the value: "))
        source_currency = input(
            "Enter the Source currency code (E.G. USD): ").upper()
        target_currency = input(
            "Enter the Target currency code (E.G. INR): ").upper()

        if source_value <= 0:
            print("Value cannot be negative or zero.")
            return

        result = convert_currency(
            source_value, source_currency, target_currency)

        print(f"{source_value} {source_currency} => {result} {target_currency}")

    except ValueError:
        print("Please enter a valid value to convert")

    except KeyError:
        print("Please double check the currencies")


if __name__ == "__main__":
    main()
