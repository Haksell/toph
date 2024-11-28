# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        dp = [0] * 31
        for _ in rir():
            p, w = mir()
            for i in range(len(dp) - 1, w - 1, -1):
                dp[i] = max(dp[i], dp[i - w] + p)
        print(sum(max(dp[: ir() + 1]) for _ in rir()))


if __name__ == "__main__":
    main()
