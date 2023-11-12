def findAverage(nums):
    total_value = 0
    if not nums:
        return total_value
    for num in nums:
        total_value += num
    return total_value // len(nums)


def main():
    print(findAverage([1, 2, 3]))  # 2
    print(findAverage([1, 2, 3, 1, 2, 3, 1, 2, 3]))  # 2
    print(findAverage([12, 20, 37]))  # 23
    print(findAverage([0, 0, 0, 0, 0]))  # 0


if __name__ == "__main__":
    main()