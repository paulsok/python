import sys

def frac_knapbag(capacity, val_weights):
    order = [(v / w, w) for v, w in val_weights]
    order.sort(reverse=True)

    acc = 0
    for v_per_w, w in order:
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        else:
            acc += v_per_w * capacity
            break

    return acc

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    val_weights = list(reader)
    assert len(val_weights) == n
    opt_val = frac_knapbag(capacity, val_weights)
    print("{:.3f}".format(opt_val))


if __name__ == '__main__':
    main()
