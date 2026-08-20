def main():
    global emoticon
    say("Is anyone there?")
    emoticon = "ovo"
    say("Oh, hello!")

def say(words):
    print(words, emoticon)

emoticon = "qaq"

main()