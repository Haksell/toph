# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MATCHING = {")": "(", "]": "[", "}": "{"}


def main():
    stack = []
    for c in input():
        closing = MATCHING.get(c)
        if not closing:
            stack.append(c)
        elif not stack or stack.pop() != closing:
            print("No")
            return
    print("No" if stack else "Yes")


if __name__ == "__main__":
    main()
