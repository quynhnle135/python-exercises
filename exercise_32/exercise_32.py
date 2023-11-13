def convertStrToInt(string):
    strToInt_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    num = 0
    isNegative = False
    if string[0] == "-":
        isNegative = True
        string = string[1:]
    while len(string) > 0:
        digit = string[0]
        num = num * 10 + strToInt_dict[digit]
        string = string[1:]
    if isNegative:
        return -num
    return num


def main():
    print(convertStrToInt("123"))
    print(type(convertStrToInt("123")))
    print(convertStrToInt("-123"))
    print(type(convertStrToInt("-123")))


if __name__ == "__main__":
    main()