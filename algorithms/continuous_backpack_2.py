import sys
import heapq


def frac_knapbag(capacity, val_weights):
    order = [(- v / w, w) for v, w in val_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

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
