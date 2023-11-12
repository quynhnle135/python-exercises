def fizzbuzz(upTo):
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


def main():
    fizzbuzz(35)


if __name__ == "__main__":
    main()