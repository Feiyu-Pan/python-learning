WORDS = {"PAIR": 4, "HAIR":4, "CHAIR":5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} left!")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
                        print("Impressive! You win!")
                        break
        if guess in WORDS:
                print(f"Good job! You scored {WORDS.pop(guess)} points!")

    print("That's the game!")

main()