# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        d, a = map(float, input().split())
        adj = d / math.tan(math.radians(a))
        hyp = math.sqrt(adj * adj + d * d)
        print(adj + hyp)


if __name__ == "__main__":
    main()
