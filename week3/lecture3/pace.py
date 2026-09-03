def main():
    miles = get_miles("Miles: ")
    minutes = get_minutes("Minutes: ")
    pace = miles / minutes
    print(f"Your speed shall be at least {round(pace,2)} miles per minute.")


def get_miles(prompt):
    while True:
        try:
            miles = int(input(prompt))
            if miles > 0:
                return miles
            else:
                raise ValueError
        except ValueError:
            pass


def get_minutes(prompt):
    while True:
        try:
            minutes = int(input(prompt))
            if minutes > 0:
                return minutes
            else:
                raise ValueError
        except ValueError:
            pass


main()