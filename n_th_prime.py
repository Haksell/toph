# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    sieve = [False, False, True, True]
    while True:
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        if len(primes) >= n:
            print(primes[n - 1])
            return
        old_len = len(sieve)
        sieve.extend([True] * old_len)
        for i in range(2, isqrt(len(sieve)) + 1):
            if sieve[i]:
                for j in range((old_len + i - 1) // i * i, len(sieve), i):
                    sieve[j] = False


if __name__ == "__main__":
    main()
