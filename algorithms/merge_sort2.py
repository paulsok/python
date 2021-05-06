def inversions_count(unsorted):
    if len(unsorted) <= 1:
        return unsorted, 0

    middle = len(unsorted) // 2
    left_list, left_list_inv = inversions_count(unsorted[:middle])
    right_list, right_list_inv = inversions_count(unsorted[middle:])
    merged, merge_inv = merge(left_list, right_list)

    return merged, left_list_inv + right_list_inv + merge_inv


def merge(left_list, right_list):
    merged = []
    i, j = 0, 0
    merge_inv = 0

    while i < len(left_list) and j < len(right_list):

        if left_list[i] <= right_list[j]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[j])
            merge_inv += (len(left_list) - i)
            j += 1

    merged.extend(left_list[i:] + right_list[j:])

    return merged, merge_inv


def main():
    unsorted = [int(i) for i in input().split()]
    sorted_, inv_count = inversions_count(unsorted)
    print(inv_count)


if __name__ == '__main__':
    main()
