def writeToFile(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def appendToFile(file_name, text):
    with open(file_name, "a") as f:
        f.write(text)


def readFromFile(file_name):
    with open(file_name, "r") as f:
        return f.read()


def main():
    writeToFile("/Users/quinnle/PycharmProjects/python-exercises/exercise_8/greet.txt", "Hello!\n")
    appendToFile("/Users/quinnle/PycharmProjects/python-exercises/exercise_8/greet.txt", "Goodbye!\n")
    print(readFromFile("/Users/quinnle/PycharmProjects/python-exercises/exercise_8/greet.txt"))


if __name__ == "__main__":
    main()