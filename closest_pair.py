# ruff: noqa: E731, E741
from bisect import bisect_left, bisect_right
from math import hypot, inf as INF
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    num_points = ir()
    xs = []
    ys = []
    points = []
    for i in range(num_points):
        x, y = mir()
        xs.append((x, i))
        ys.append((y, i))
        points.append((x, y))
    xs.sort()
    ys.sort()
    closest_pair = INF
    for i1, (x1, y1) in enumerate(points):
        lo_x = bisect_left(xs, (x1 - closest_pair, -INF))
        hi_x = bisect_right(xs, (x1 + closest_pair, INF))
        lo_y = bisect_left(ys, (y1 - closest_pair, -INF))
        hi_y = bisect_right(ys, (y1 + closest_pair, INF))
        dx = hi_x - lo_x
        dy = hi_y - lo_y
        point_indexes = (
            (xs[j][1] for j in range(lo_x, hi_x))
            if dx < dy
            else (ys[j][1] for j in range(lo_y, hi_y))
        )
        for i2 in point_indexes:
            if i1 < i2:
                x2, y2 = points[i2]
                closest_pair = min(closest_pair, hypot(x1 - x2, y1 - y2))
    print(closest_pair)


if __name__ == "__main__":
    main()
