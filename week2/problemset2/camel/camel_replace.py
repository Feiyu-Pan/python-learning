def main():
    name = input("camelCase: ")
    for letter in name:
        if letter.isupper():
            name = name.replace(letter, f"_{letter.lower()}")
    print(f"snake_case: {name}")


main()