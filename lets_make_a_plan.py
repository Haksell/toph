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
        tom1, tom2, john1, john2 = input().split()
        tom = {tom1, tom2}
        john = {john1, john2}
        print("Possible" if tom & john else "Oh no!, such a shame")


if __name__ == "__main__":
    main()
