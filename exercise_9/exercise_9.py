def getChessSquareColor(column, row):
    if row <= 0 or row > 8 or column <= 0 or column > 8:
        return ""
    if column % 2 == 0 and row % 2 == 0:
        return "white"
    elif column % 2 != 0 and row % 2 != 0:
        return "white"
    else:
        return "black"


def main():
    print(getChessSquareColor(1, 1))
    print(getChessSquareColor(2, 1))


if __name__ == "__main__":
    main()