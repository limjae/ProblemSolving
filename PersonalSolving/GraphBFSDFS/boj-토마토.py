# https://www.acmicpc.net/problem/7576
from collections import defaultdict
from collections import deque
col, row = list(map(int, input().split()))
#  정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
dX = [0, 1, 0, -1]
dY = [1, 0, -1, 0]

tomato_map = []
tomato_count = defaultdict(int)


for _ in range(row):
    tomato_map.append(list(map(int, input().split())))

for y, rows in enumerate(tomato_map):
    for x, value in enumerate(rows):
        tomato_count[value] += 1


if tomato_count[0] == 0:
    print("0", end="")
else:
    tomato_deque = deque()
    for y in range(row):
        for x in range(col):
            if tomato_map[y][x] == 1:
                tomato_deque.append((y, x))

    if tomato_count[0] == 0:
        print("0", end="")

    days = -1
    while tomato_deque:
        new_tomato_deque = deque()
        for y, x in tomato_deque:
            for d in range(4):
                new_x = x + dX[d]
                new_y = y + dY[d]
                if 0 <= new_y < row and 0 <= new_x < col and tomato_map[new_y][new_x] == 0:
                    tomato_map[new_y][new_x] = 1
                    tomato_count[0] -= 1
                    new_tomato_deque.append((new_y, new_x))

        tomato_deque = new_tomato_deque
        days += 1

    if tomato_count[0] == 0:
        print(days, end="")
    else:
        print(-1, end="")
