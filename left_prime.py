# ruff: noqa: E731, E741
from bisect import bisect_left
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_primes(lim):
    sieve = [True] * lim
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(lim) + 1):
        if sieve[i]:
            for j in range(i * i, lim, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def main():
    primes = get_primes(10_000_001)
    for _ in rir():
        print(bisect_left(primes, ir()))


if __name__ == "__main__":
    main()
