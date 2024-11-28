# ruff: noqa: E731, E741
from itertools import count
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    LIM = 10**9
    seq = [1]
    rev = {1: 1}
    for i in count(2):
        j = (i >> 1) - 1
        new = seq[j] * seq[j + 1] + 2 if i & 1 else seq[j] ** 2 + 1
        if new > LIM:
            break
        seq.append(new)
        rev[new] = i
    for i in rir():
        print(f"Case {i+1}: {rev[ir()]}")


if __name__ == "__main__":
    main()
