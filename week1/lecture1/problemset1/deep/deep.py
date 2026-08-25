def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if forty_two(answer):
        print("Yes")
    else:
        print("No")

def forty_two(a):
    return a.strip() == "42" or a.strip().lower() == "forty-two" or a.strip().lower() == "forty two"

main()