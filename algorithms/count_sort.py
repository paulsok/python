def counting_sort(n, numbers):
    B = [0] * 11
    result = [0] * n

    for i in numbers:
        B[i] += 1

    for i in range(1, 11):
        B[i] += B[i - 1]

    for i in range(n - 1, -1, -1):
        result[B[numbers[i]] - 1] = numbers[i]
        B[numbers[i]] -= 1

    return result


def main():
    n = int(input())
    numbers = [int(i) for i in input().split()]
    print(' '.join(map(str, counting_sort(n, numbers))))


if __name__ == '__main__':
    main()
