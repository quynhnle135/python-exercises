def getUpperCase(text):
    upper_dict = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}
    uppercase_text = ""
    for letter in text:
        if letter in upper_dict:
            uppercase_text += upper_dict[letter]
        else:
            uppercase_text += letter
    return uppercase_text


def main():
    print(getUpperCase("Hello"))
    print(getUpperCase("I lOvE PyThon"))


if __name__ == "__main__":
    main()