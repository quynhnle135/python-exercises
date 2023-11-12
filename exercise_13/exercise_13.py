def calculateSum(nums):
    total_value = 0
    if not nums:
        return total_value

    for num in nums:
        total_value += num
    return total_value


def calculateProduct(nums):
    product = 1
    if not nums:
        return product

    for num in nums:
        product *= num
    return product


def main():
    print(calculateSum([2, 4, 6, 8, 10]))  # 30
    print(calculateProduct([2, 4, 6, 8, 10]))  # 3840


if __name__ == "__main__":
    main()