def mergeTwoLists(list1, list2):
    res = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            res.append(list2[j])
            j += 1
        else:
            res.append(list1[i])
            i += 1
    while i < len(list1):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1
    return res


def main():
    print(mergeTwoLists([1, 3, 6], [5, 7, 8, 9]))


if __name__ == "__main__":
    main()