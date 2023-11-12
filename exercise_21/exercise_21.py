def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def isValidDate(year, month, day):
    if year <= 0:
        return False
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
        return False
    elif month in [4, 6, 9, 11] and not (1 <= day <= 30):
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and day == 29 and not isLeapYear(year):
        return False
    return True


def main():
    pass


if __name__ == "__main__":
    main()