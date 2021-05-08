import sys
import random


def partition(array: list, start: int, end: int):
    if end - start >= 2:
        m = random.randint(start, end - 1)
        i, j, k = start + 1, start, start
        array[start], array[m] = array[m], array[start]

        for i in range(start + 1, end):
            if array[i] < array[start]:
                k += 1
                j += 1
                array[i], array[j] = array[j], array[i]
                array[k], array[j] = array[j], array[k]

            elif array[i] == array[start]:
                j += 1
                array[i], array[j] = array[j], array[i]

        array[start], array[k] = array[k], array[start]
        return j, k

    return -1, -1


def quick_sort(array: list, start: int, end: int):

    i, k = partition(array, start, end)

    if i != -1:
        quick_sort(array, start, k)
        quick_sort(array, i + 1, end)


def get_count_equal_or_less(array: list, point: int, start: int, end: int):

    if end - start >= 2:
        center = int((start + end) / 2)

        if point >= array[center]:
            return center - start + get_count_equal_or_less(array, point, center, end)

        return get_count_equal_or_less(array, point, start, center)

    elif array[start] <= point:
        return 1

    return 0


def get_count_less(array: list, point: int, start: int, end: int):

    if end - start >= 2:
        center = int((start + end)/2)

        if point > array[center]:
            return center - start + get_count_less(array, point, center, end)

        return get_count_less(array, point, start, center)

    elif array[start] < point:
        return 1

    return 0


def main():
    n, _ = map(int, sys.stdin.readline().split())
    ranges_x, ranges_y = [], []

    for i in range(n):
        x, y = map(int, input().split())
        ranges_x.append(x)
        ranges_y.append(y)

    points = list(map(int, sys.stdin.readline().split()))
    quick_sort(ranges_x, 0, n)
    quick_sort(ranges_y, 0, n)

    for point in points:
        print(get_count_equal_or_less(ranges_x, point, 0, n) -
              get_count_less(ranges_y, point, 0, n), end=' ')


if __name__ == '__main__':
    main()
