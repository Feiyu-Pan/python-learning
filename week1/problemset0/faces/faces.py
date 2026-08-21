def main():
    print(convert(input("You alright? ")))

def convert(response):
    return(response.replace(":)", "🙂").replace(":(", "🙁"))

main()