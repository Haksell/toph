# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for case in rir():
        s = input()
        space = s.index(" ")
        il = space - 1
        ir = len(s) - 1
        res = []
        carry = 0
        while il >= 0 or ir > space:
            if il >= 0:
                carry += ord(s[il]) - 48
            if ir > space:
                carry += ord(s[ir]) - 48
            carry, d = divmod(carry, 10)
            res.append(d)
            il -= 1
            ir -= 1
        if carry:
            res.append(carry)
        print(f"Case #{case+1}:", "".join(map(str, reversed(res))))


if __name__ == "__main__":
    main()
