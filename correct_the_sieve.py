# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_sieve(lim):
    sieve = [True] * lim
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(lim) + 1):
        if sieve[i]:
            for j in range(i * i, lim, i):
                sieve[j] = False
    return sieve


def main():
    sieve = get_sieve(1_000_001)
    for _ in rir():
        n = ir()
        print(f"{n} is {'' if sieve[n] else 'not '}a prime number.")


if __name__ == "__main__":
    main()
