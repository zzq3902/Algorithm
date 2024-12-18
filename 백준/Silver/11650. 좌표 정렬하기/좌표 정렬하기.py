# sort 와 lambda 함수를 사용하여 정렬한다.

import sys


input = sys.stdin.readline
N = int(input())
points = [list(map(int, input().split()))for _ in range(N)]
points.sort()
for point in points:
    sys.stdout.write(f'{point[0]} {point[1]}\n')
