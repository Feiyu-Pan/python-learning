def main():
    size = int(input("What's the size? "))
    create_square(size)

def create_square(size):
    for _ in range(size):
        print("#" * size)

main()