def main():
    vowels = {"a", "e", "i", "o", "u"}

    input_ = input("Input: ")
    output_ = "".join(
        "" if i.lower() in vowels else i
        for i in input_
    )

    print(f"Output: {output_}")


main()