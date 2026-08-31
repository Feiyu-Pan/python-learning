def main():
    history = []
    arrows = {"\x1b[A": "⬆️", 
                  "\x1b[B": "⬇️", 
                  "\x1b[C": "➡️", 
                  "\x1b[D": "⬅️"
        }
        
    while True:
        action = (input("Action: "))
        if action == "-":
            if history == []:
                print("No actions yet.")
            else:
                print(f"Undone: {history.pop()}")       
        elif action == "`":
            history.clear()
            print("Game restarts.")
        elif action in arrows:
            action = arrows[action]
            history.append(action)
        else:
            print("Please input a valid action.")

        if history != []:
            print(" ".join(history))


main()