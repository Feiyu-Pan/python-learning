def main():
    # Ask user for their name
    name = input("What's your name? ")
    # Remove white spaces from str and capitalise
    name = name.strip().title()
    # Split user's name into first name and last name
    first, last =  name.split(" ")
    # Say hello to user
    hello(first)

def hello(user):
    print("Hello, ", user, "!", sep="")

main()