def bottlesOfBeer(num):
    for i in range(num, 0, -1):
        print(f"{i} bottles of beer on the wall,\n"
              f"{i} bottles of beer,\n"
              f"Take one down,\n"
              f"Pass it around,")
    print("No more bottles of beer on the wall!")


def main():
    bottlesOfBeer(10)


if __name__ == "__main__":
    main()