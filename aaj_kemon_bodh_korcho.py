# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_fibo(lim):
    fibo = [0, 1]
    while fibo[-1] < lim:
        fibo.append(fibo[-1] + fibo[-2])
    return set(fibo)


def main():
    fibo = get_fibo(10**5)
    for case in rir():
        barca = sum(
            1 if c == "B" else -1 for i, c in enumerate(input()) if i not in fibo
        )
        res = (
            "Aaj Kemon Bodh Korcho"
            if barca > 0
            else "Hala Madrid"
            if barca < 0
            else "Meh :\\"
        )
        print(f"Case #{case+1}: {res}")


if __name__ == "__main__":
    main()
