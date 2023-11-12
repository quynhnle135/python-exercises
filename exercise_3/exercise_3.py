def isOdd(num):
    if type(num) == float:
        return False
    return num % 2 != 0


def isEven(num):
    if type(num) == float:
        return False
    return num % 2 == 0


def main():
    print(isOdd(42))  # False
    print(isOdd(9999))  # True
    print(isOdd(-10))  # False
    print(isOdd(-11))  # True
    print(isOdd(3.1415))  # False

    print(isEven(42))  # True
    print(isEven(9999))  # False
    print(isEven(-10))  # True
    print(isEven(-11))  # False
    print(isEven(3.1415))  # False



if __name__ == "__main__":
    main()