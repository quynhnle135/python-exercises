def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))


def main():
    printASCIITable()


if __name__ == "__main__":
    main()