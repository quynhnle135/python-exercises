def ordinalSuffix(num):
    suffix_dict = {"1": "st", "2": "nd", "3": "rd", "11": "th"}
    num = str(num)
    if num.endswith("11") or num.endswith("12") or num.endswith("13"):
        return num + suffix_dict["11"]
    elif num.endswith("1"):
        return num + suffix_dict["1"]
    elif num.endswith("2"):
        return num + suffix_dict["2"]
    elif num.endswith("3"):
        return num + suffix_dict["3"]
    else:
        return num + "th"


def ordinal_suffix(num):
    num = str(num)
    if num[-2:] in ["11", "12", "13"]:
        return num + "th"
    elif num[-1] == "1":
        return num + "st"
    elif num[-1] == "2":
        return num + "nd"
    elif num[-1] == "3":
        return num + "rd"
    else:
        return num + "th"


def main():
    print(ordinalSuffix(1))
    print(ordinalSuffix(2))
    print(ordinalSuffix(3))
    print(ordinalSuffix(4))
    print(ordinalSuffix(10))
    print(ordinalSuffix(11))
    print(ordinalSuffix(12))
    print(ordinalSuffix(13))
    print(ordinalSuffix(14))
    print(ordinalSuffix(101))
    print("---")
    print(ordinal_suffix(1))
    print(ordinal_suffix(2))
    print(ordinal_suffix(3))
    print(ordinal_suffix(4))
    print(ordinal_suffix(10))
    print(ordinal_suffix(11))
    print(ordinal_suffix(12))
    print(ordinal_suffix(13))
    print(ordinal_suffix(14))
    print(ordinal_suffix(101))

if __name__ == "__main__":
    main()