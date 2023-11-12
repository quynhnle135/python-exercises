def getSmallest(nums):
    smallest = float("inf")
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest


def getBiggest(nums):
    biggest = float("-inf")
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest


def main():
    print(getSmallest([28, 25, 42, 2, 28]))
    print(getBiggest([28, 25, 42, 2, 28]))


if __name__ == "__main__":
    main()