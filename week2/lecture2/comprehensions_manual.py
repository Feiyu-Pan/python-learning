def main():
    words = get_words("address.txt")
    lowercase_words = []
    for word in words:
        if word != "—":
            lowercase_words.append(word.lower().strip(",."))

    counts = {}
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

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