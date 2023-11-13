def drawRectangle(width, length):
    if width < 1 or length < 1:
        return
    for i in range(length):
        for j in range(width):
            print("#", end="")
        print()


def main():
    drawRectangle(16, 4)


if __name__ == "__main__":
    main()