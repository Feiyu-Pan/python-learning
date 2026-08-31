import random


def sample(moisture):
    return moisture - random.randint(3, 8)


def main():
    moisture = 50
    days = 0
    print(f"Day {days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample(moisture)
        days += 1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")


main()