def findAndReplace(text, oldText, newText):
    replacedText = ""
    i = 0
    while i < len(text):
        if text[i: i + len(oldText)] == oldText:
            replacedText += newText
            i = i + len(oldText)
        else:
            replacedText += text[i]
            i += 1
    return replacedText


def main():
    print(findAndReplace("The fox", "fox", "dog"))
    print(findAndReplace("foxfox", "fox", "dog"))


if __name__ == "__main__":
    main()