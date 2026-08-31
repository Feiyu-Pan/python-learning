def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower().strip(",.") for word in words if word != "—"]

    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    save_counts(counts)


def get_words(filename):
    with open(filename, "r") as file:
        contents = file.read()
        return contents.split()


def save_counts(counts):
    with open("counts.csv", "w") as file:
        for word, count in counts.items():
            file.write(f"{word}: {count}\n")


main()