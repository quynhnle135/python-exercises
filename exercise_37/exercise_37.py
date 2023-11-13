def makeChange(amount):
    change = {}
    if amount >= 25:
        change['quarters'] = amount // 25
        amount = amount % 25
    if amount >= 10:
        change['dimes'] = amount // 10
        amount = amount % 10
    if amount >= 5:
        change['nickles'] = amount // 5
        amount = amount % 5
    if amount >= 1:
        change['pennies'] = amount
    return change


def main():
    print(makeChange(125))
    print(makeChange(127))


if __name__ == "__main__":
    main()
