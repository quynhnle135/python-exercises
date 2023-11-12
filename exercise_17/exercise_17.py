from random import randint

def rollDice(numberOfDice):
    total = 0
    for i in range(numberOfDice):
        total += randint(1, 6)
    return total


def main():
    print(rollDice(1))
    print(rollDice((3)))


if __name__ == "__main__":
    main()