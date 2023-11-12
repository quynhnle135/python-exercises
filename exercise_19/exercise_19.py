import random


def generatePassword(length):
    LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "1234567890"
    SPECIAL = "~!@#$%^&*()_+"
    if length < 12:
        length = 12

    ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    password = []
    password.append(LOWER_LETTERS[random.randint(0, len(LOWER_LETTERS) - 1)])
    password.append(UPPER_LETTERS[random.randint(0, len(UPPER_LETTERS) - 1)])
    password.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
    password.append(SPECIAL[random.randint(0, len(SPECIAL) - 1)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, len(SPECIAL) - 1)])

    random.shuffle(password)
    return "".join(password)


def main():
    print(generatePassword(12))
    print(generatePassword(20))


if __name__ == "__main__":
    main()
