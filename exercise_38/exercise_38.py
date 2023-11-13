import random


def shuffle(values):
    for i in range(len(values)):
        randomIdx = random.randint(0, len(values) - 1)
        values[i], values[randomIdx] = values[randomIdx], values[i]
    return values


def main():
    print(shuffle([1, 2, 3, 4, 5]))
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == "__main__":
    main()