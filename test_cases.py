# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    cases, time_limit, memory_limit = mir()

    for _ in range(cases):
        diff, time_used, memory_used = mir()
        if time_used > time_limit:
            print("CLE")
            return
        if memory_used > memory_limit:
            print("MLE")
            return
        if diff != 0:
            print("WA")
            return
    print("AC")


if __name__ == "__main__":
    main()
