# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

LIM = 1_000_001


def main():
    phi = list(range(LIM))
    phi[1] = 0
    for i in range(2, LIM):
        if phi[i] == i:
            for j in range(i, LIM, i):
                phi[j] -= phi[j] // i

    for _ in rir():
        n = ir()
        print((n - phi[n] - 1) * n >> 1)


if __name__ == "__main__":
    main()
