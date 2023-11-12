def multiplicationTableGenerate():
    for row in range(1, 11):
        for col in range(1, 11):
            print(row * col, end=" ")
        print()


def main():
   multiplicationTableGenerate()


if __name__ == "__main__":
    main()