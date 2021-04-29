def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m ** 2):
        previous, current = current, (previous + current) % m

        if (previous == 0 and current == 1):
            return i + 1


def fib_mod(n, m):
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period

    previous, current = 0, 1

    if n <= 1:
        return n

    for i in range(n - 1):
        previous, current = current, previous + current

    return (current % m)


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
