def rot13(text):
    encryptedText = ""
    for character in text:
        if not character.isalpha():
            encryptedText += character
        else:
            rotatedLetterOrdinal = ord(character) + 13
            if character.islower() and rotatedLetterOrdinal > 122:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26
            encryptedText += chr(rotatedLetterOrdinal)
    return encryptedText


def main():
    print(rot13("Hello, world"))


if __name__ == "__main__":
    main()