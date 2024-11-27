# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, i, value):
        i += self.n
        self.tree[i] = value
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def range_sum(self, left, right):
        left += self.n
        right += self.n
        res = 0
        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                res += self.tree[right]
            left >>= 1
            right >>= 1
        return res


def get_primes(lim):
    sieve = [True] * lim
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(lim) + 1):
        if sieve[i]:
            for j in range(i * i, lim, i):
                sieve[j] = False
    return {i for i, is_prime in enumerate(sieve) if is_prime}


def main():
    primes = get_primes(10**7 + 1)
    _ = ir()
    seg = SegmentTree([int(n in primes) for n in mir()])
    for _ in rir():
        q, x, y = mir()
        if q == 1:
            print(seg.range_sum(x - 1, y))
        else:
            seg.update(x - 1, int(y in primes))


if __name__ == "__main__":
    main()
