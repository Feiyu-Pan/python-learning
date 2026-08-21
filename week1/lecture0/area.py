def main():
    # Ask user for lengths and widths
    a = float(input("What's the length of the house? "))
    b = float(input("What's the width of the house? "))
    c = float(input("What's the length of the yard? "))
    d = float(input("What's the width of the yard? "))
    # Calculate the total area
    print("The total area is", area(a, b) + area(c, d), "suqare feet.")

def area(length, width):
    return length * width

main()