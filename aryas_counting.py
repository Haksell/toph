# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for i in rir():
        a, b, c = mir()
        print(
            f"Case {i+1}:",
            "A"
            if a > b and a > c
            else "B"
            if b > a and b > c
            else "C"
            if c > a and c > b
            else "Confused",
        )


if __name__ == "__main__":
    main()
