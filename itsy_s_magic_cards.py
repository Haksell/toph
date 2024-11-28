# ruff: noqa: E731, E741
from collections import defaultdict
from itertools import combinations
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    num_cards, lines = mir()

    bidict = defaultdict(list)
    for _ in range(lines):
        a, b = input().split()
        bidict[a].append(b)
        bidict[b].append(a)

    cards = list(map(chr, range(65, 65 + num_cards)))

    max_cards = max(
        r
        for r in range(len(cards) + 1)
        for subset in combinations(cards, r=r)
        if all(k2 not in bidict[k1] for k1 in subset for k2 in subset)
    )
    print(max_cards)


if __name__ == "__main__":
    main()
