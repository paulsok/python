def position(A, i):
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo + hi) // 2
        if i < A[mid]:
            hi = mid
        elif i > A[mid]:
            lo = mid + 1
        else:
            return mid + 1
    
    return - 1


def main():
    n, *A = map(int, input().split())
    k, *numbers = map(int, input().split())

    for i in numbers:
        print(position(A, i), end=" ")


if __name__ == "__name__":
    main()
