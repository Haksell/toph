# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    t, w = mir()
    print(
        "Bandor, these bananas are tasty enough."
        if t > 2000 or (t > 0 and w > 100)
        else "No Bandor, bananas are not tasty enough."
    )


if __name__ == "__main__":
    main()
