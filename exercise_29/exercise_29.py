def drawParamid(height):
    space = height - 1
    star = 1
    for i in range(height):
        print((space * " " + (star * "#")))
        space -= 1
        star += 2


def main():
    drawParamid(7)


if __name__ == "__main__":
    main()