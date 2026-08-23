name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Cedric" | "Newt":
        print("Hufflepuff")
    case "Luna" | "Cho":
        print("Ravenclaw")
    case "Draco" | "Feiyu":
        print("Slytherin")
    case _:
        print("Who?")