def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def main():
    pass


if __name__ == "__main__":
    main()