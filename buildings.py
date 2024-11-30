# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(k, h):
    cnt = Counter(h)
    keys = sorted(cnt.keys())
    for a, b in zip(keys, keys[1:]):
        total_cost = (b - a) * cnt[a]
        if total_cost > k:
            return a + k // cnt[a]
        k -= total_cost
        cnt[b] += cnt[a]
        del cnt[a]
    height, quantity = next(iter(cnt.items()))
    return height + k // quantity


def main():
    _, k = mir()
    h = lmir()
    print(solve(k, h))


if __name__ == "__main__":
    main()
