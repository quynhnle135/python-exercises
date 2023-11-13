def collatz(num):
    if num == 0:
        return []
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    sequence.append(num)
    return sequence


def main():
    print(collatz(10))
    print(collatz(11))


if __name__ == "__main__":
    main()