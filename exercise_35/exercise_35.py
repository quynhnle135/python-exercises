def getTitleCase(text):
    titledText = ""
    for i in range(len(text)):
        if i == 0:
            titledText += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        else:
            titledText += text[i].lower()

    return titledText


def main():
    print(getTitleCase("HeLLo"))
    print(getTitleCase("hELLO@wORLd"))


if __name__ == "__main__":
    main()