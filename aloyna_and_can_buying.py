# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    _, k = mir()
    cnt = [0] * (k + 1)
    for x in mir():
        cnt[x] += 1
    print(max(range(k + 1), key=lambda i: (cnt[i], -i)))


if __name__ == "__main__":
    main()
