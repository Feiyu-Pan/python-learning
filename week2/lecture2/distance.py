def main():
    distances = {
        "Burger": 163,
        "Egg": 101, 
        "Bro": 79
    }
    for name, distance in distances.items():
        print(f"{name} is {distance} AU away from Earth, e.g. {convert(distance)} metres.")

def convert(au):
    return au * 149597870700
   

main()