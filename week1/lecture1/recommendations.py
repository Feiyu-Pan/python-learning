def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Please enter a valid difficulty.")
        return
    players = input("Mutiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Please enter a valid number of players.")
    else:
        print("You might like", recommend(difficulty, players),)

def recommend(d, p):
    if d == "Difficult" and p == "Multiplayer":
            return("Brass: Brimingam.")
    elif d == "Difficult" and p == "Single-player":
            return("Mage Knight.")
    elif d == "Casual" and p == "Multiplayer":
            return("Heat.")
    else:
            return("Friday.")

main()