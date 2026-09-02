def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    No_1 = s.isalnum() 
    No_2 = s[:2].isalpha()
    No_3 = len(s) in range (2, 7)
    No_4 = s.rstrip("0123456789").isalpha()
    numbers = "".join(
        "" if char.isalpha() else char
        for char in s
    )
    No_5 = numbers[0] != "0" if numbers != "" else True
    
    return No_1 and No_2 and No_3 and No_4 and No_5


main()