def commaFormat(num):
    # Convert input number to string
    num = str(num)

    # Remove the fractional part
    if "." in num:
        fractional = num[num.index("."):]
        num = num[:num.index(".")]
    else:
        fractional = ""

    triplet = ""
    commaNumber = ""

    for i in range(len(num) - 1, -1, -1):
        triplet = num[i] + triplet
        if len(triplet) == 3:
            commaNumber = triplet + "," + commaNumber
            triplet = ""
    if triplet != "":
        commaNumber = triplet + "," + commaNumber

    return commaNumber[:-1] + fractional


def main():
    string = "123.4566"
    print(string.index("."))
    new_string = string[:string.index(".")]
    print(new_string)

    print(commaFormat("10000"))
    print(commaFormat("1000"))
    print(commaFormat("1234567890"))
    print(commaFormat("1234.678909"))

if __name__ == "__main__":
    main()