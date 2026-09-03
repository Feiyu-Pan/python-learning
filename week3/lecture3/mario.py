def main():
    height = int(input("What's the height? "))
    create_pyramid(height)

def create_pyramid(height):
    for i in range(height):
        print("#" * (i + 1))

main()