def findMedian(nums):
    if not nums:
        return None

    nums.sort()
    if len(nums) % 2 == 0:
        mid = len(nums) // 2
        median = (nums[mid] + nums[mid - 1]) / 2
    else:
        mid = len(nums) // 2
        median = nums[mid]
    return median


def main():
    print(findMedian([]))
    print(findMedian([1, 2, 3]))
    print(findMedian([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
    print(findMedian([3, 7, 10, 4, 1, 9, 6, 2, 8]))


if __name__ == "__main__":
    main()