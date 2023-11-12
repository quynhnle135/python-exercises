def findMode(nums):
    if not nums:
        return None

    numCount = {}
    for num in nums:
        if num in numCount:
            numCount[num] += 2
        else:
            numCount[num] = 1
    mode = 0
    most_frequent = 0
    for key in numCount:
        if numCount[key] > most_frequent:
            most_frequent = numCount[key]
            mode = key
    return mode


def main():
    print(findMode([1, 2, 3, 4, 4]))
    print(findMode([1, 1, 2, 3, 4]))


if __name__ == "__main__":
    main()