def main():
    name = input("camelCase: ")
    snake_case = ""
    for letter in name:
        if letter.isupper():
            snake_case += f"_{letter.lower()}"
        else:
            snake_case += letter
    print(f"snake_case: {snake_case}")


main()