shows = [
    "patrick the star ",
    " uchiha sasuke",
    "zou ZHIYUAN",
    "hamburglar"
]


def main():
    cleaned_shows = []
    for show in shows:
        cleaned_shows.append(show.strip().lower().title())
    print(", ".join(cleaned_shows))

main()