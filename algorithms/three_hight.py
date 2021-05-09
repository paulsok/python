def tree_height(parents):
    depths = [-1] * (len(parents)) + [0]

    def count_depth(i):
        if depths[i] == -1:
            depths[i] = count_depth(parents[i]) + 1
        return depths[i]

    return max(count_depth(i) for i in range(len(parents)))


def main():
    parents = [int(i) for i in input().split()]
    print(tree_height(parents))


if __name__ == '__main__':
    main()
