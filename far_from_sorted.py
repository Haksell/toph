# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def mergesort(arr, lo, hi):
    if lo == hi:
        return [arr[lo]], 0
    mi = lo + hi >> 1
    arr_left, inv_left = mergesort(arr, lo, mi)
    arr_right, inv_right = mergesort(arr, mi + 1, hi)
    inv = inv_left + inv_right
    out = []
    li = ri = 0
    while li < len(arr_left) or ri < len(arr_right):
        if ri == len(arr_right) or (
            li < len(arr_left) and arr_left[li] <= arr_right[ri]
        ):
            out.append(arr_left[li])
            li += 1
        else:
            out.append(arr_right[ri])
            ri += 1
            inv += len(arr_left) - li
    return out, inv


def main():
    n = ir()
    a = lmir()
    _, inversions = mergesort(a, 0, n - 1)
    print(inversions)


if __name__ == "__main__":
    main()
