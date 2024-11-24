# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    shift = ir()
    plaintext = input()
    print(
        "".join(
            chr(((ord(c) & 31) - 1 - shift) % 26 + 97) if c.islower() else c
            for c in plaintext
        )
    )


if __name__ == "__main__":
    main()
