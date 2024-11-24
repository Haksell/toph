# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n & 1 == 0:
        return False
    else:
        return all(n % i > 0 for i in range(3, isqrt(n) + 1, 2))


def main():
    n = ir()
    if is_prime(n):
        print("NO PUNISHMENT")
    else:
        for _ in range(n):
            print("I DID NOT DO THE ASSIGNMENT.")


if __name__ == "__main__":
    main()
