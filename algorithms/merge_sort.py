def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid
# Merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1
# Copy in the rest of the start to mid sequence
    while i < mid:
        lst.append(seq[i])
        i += 1

    for i in range(len(lst)):
        seq[start+i] = lst[i]

    return seq


def mergeSortRecursively(seq, start, stop):
    # We must use >= here only when the sequence we are sorting is empty.
    # Otherwise start == stop-1 in the base case.
    if start >= stop-1:
        return
    mid = (start + stop) // 2
    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

    return seq


def main():
    seq = [28, 73, 62, 16, 95, 6, 2, 9785, 97, 82]
    print(seq)
    new_seq = mergeSortRecursively(seq, 0, len(seq))
    print(new_seq)


if __name__ == "__main__":
    main()
