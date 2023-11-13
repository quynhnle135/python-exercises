def convertIntToStr(num):
    if num == 0:
        return "0"

    intToStr_dict = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}

    isNegative = False
    if num < 0:
        isNegative = True

    num = abs(num)
    num_str = ""

    while num > 0:
        digit = num % 10
        num_str = intToStr_dict[digit] + num_str
        num //= 10

    if isNegative:
        num_str = "-" + num_str
    return num_str


def main():
    print(convertIntToStr(123))
    print(type(convertIntToStr(123)))


if __name__ == "__main__":
    main()