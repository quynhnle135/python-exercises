def drawBorder(width, height):
    if width < 2 or height < 2:
        return

    # print the top
    print("+" + ("-" * (width - 2)) + "+")
    for i in range(height - 2):
        print("|" + (" " * (width - 2)) + "|")
    # print the bottom
    print("+" + ("-" * (width - 2)) + "+")


def main():
    drawBorder(16, 4)


if __name__ == "__main__":
    main()
