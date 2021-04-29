def fib(n):
    # put your code here
    fibb = list(range(n + 1))
    fibb[0], fibb[1] = 0, 1

    for i in range(len(fibb) - 2):
        fibb[i + 2] = fibb[i + 1] + fibb[i]

    return fibb[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
