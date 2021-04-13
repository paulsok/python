def select(seq, start):
    min_index = start
    for i in range(start+1, len(seq)):
        if seq[min_index] > seq[i]:
            min_index = i
    return min_index


def selectSort(seq):
    for i in range(len(seq) - 1):
        min_index = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[min_index]
        seq[min_index] = tmp
    return seq


def main():
    arr = [4, 45, 7, 678, 4, 2, 5, 6, 7]
    print(arr)
    new_arr = selectSort(arr)
    print(new_arr)


if __name__ == "__main__":
    main()
