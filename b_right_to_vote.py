# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    print(
        "Sorry, you are too young to vote."
        if n < 21
        else "Wait a little more to vote."
        if n < 23
        else "Yes, you can vote."
    )


if __name__ == "__main__":
    main()
