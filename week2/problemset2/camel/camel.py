def main():
    name = input("camelCase: ")
    snake_case = "".join(
        f"_{letter.lower()}" if letter.isupper()
        else letter
        for letter in name
    )
    print(f"snake_case: {snake_case}")

main()