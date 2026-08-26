def main():
    greetings = input("Say some greetings. ")
    if hello(greetings):
        print("$0")
    elif h(greetings):
        print("$20")
    else:
        print("$100")

def hello(g):
    return g.lstrip().lower().startswith("hello")

def h(g):
    return g.lstrip().lower().startswith("h")

main()