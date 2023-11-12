def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    total = 0
    cupsUntilFreeCoffee = 8
    while numberOfCoffees > 0:
        numberOfCoffees -= 1
        total += pricePerCoffee
        if cupsUntilFreeCoffee == 0:
            total -= pricePerCoffee
            cupsUntilFreeCoffee = 8
        else:
            cupsUntilFreeCoffee -=1
    return total


def main():
    # print(getCostOfCoffee(7, 2.50))
    # print(getCostOfCoffee(8, 2.50))
    print(getCostOfCoffee(9, 2.50))  # 20.0


if __name__ == "__main__":
    main()