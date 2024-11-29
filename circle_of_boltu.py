# ruff: noqa: E731, E741
from bisect import bisect_left, bisect_right
from itertools import chain
from math import hypot, inf as INF
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def farthest_pair(points):
    xs = []
    ys = []
    for i, (x, y) in enumerate(points):
        xs.append((x, i))
        ys.append((y, i))
    xs.sort()
    ys.sort()
    farthest_pair = -1
    for i1, (x1, y1) in enumerate(points):
        lo_x = bisect_left(xs, (x1 - farthest_pair, -INF))
        hi_x = bisect_right(xs, (x1 + farthest_pair, INF))
        lo_y = bisect_left(ys, (y1 - farthest_pair, -INF))
        hi_y = bisect_right(ys, (y1 + farthest_pair, INF))
        point_indexes = (
            (xs[j][1] for j in chain(range(lo_x), range(hi_x, len(points))))
            if lo_x - hi_x < lo_y - hi_y
            else (ys[j][1] for j in chain(range(lo_y), range(hi_y, len(points))))
        )
        for i2 in point_indexes:
            if i1 < i2:
                x2, y2 = points[i2]
                farthest_pair = max(farthest_pair, hypot(x1 - x2, y1 - y2))
    return farthest_pair


def main():
    for case in rir():
        points = [tuple(mir()) for _ in rir()]
        print(f"Case {case+1}: {round(farthest_pair(points)**2)}")


if __name__ == "__main__":
    main()
