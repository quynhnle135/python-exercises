def printHandshakes(people):
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            print(people[i], "shakes hans with", people[j])


def main():
    printHandshakes(["Alice", "Bob", "Carol", "David"])


if __name__ == "__main__":
    main()