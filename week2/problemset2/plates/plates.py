def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s):
    if not 1 < len(s) < 7:
        return False
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    for i, char in enumerate(s):
        if char.isdigit():
            return char != "0" and s[i:].isdigit()

    return True


main()