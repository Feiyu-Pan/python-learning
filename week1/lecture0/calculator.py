def main():
    # Ask user for the values of x and y
    x = float(input("What's x? "))
    y = float(input("What's y? "))
    #calculate
    print("x devided by y is", round(quotient(x, y), 2))

def quotient(dividend, divisor):
    return dividend / divisor

main()