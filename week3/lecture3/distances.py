distances = {
    "Burger": 163,
    "Egg": 101, 
    "Bro": 79
    }


def main():
    spacecraft = get_spacecraft("Enter a spacecraft: ")
    print(f"Distance: {convert(spacecraft)}m")


def get_spacecraft(prompt):
    while True:
        try:
            return distances[input(prompt)]
        except KeyError:
            pass


def convert(au):
    return au * 149597870700
   

main()