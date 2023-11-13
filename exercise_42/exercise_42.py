def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def main():
    print(bubbleSort([2, 0, 4, 1, 3]))


if __name__ == "__main__":
    main()