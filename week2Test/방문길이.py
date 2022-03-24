# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
from collections import defaultdict


def solution(dirs):
    answer = 0
    # Key = From x,y string // Value = dir string Set
    path = defaultdict(set)
    cur_x = 0
    cur_y = 0
    for direction in dirs:

        if direction == "U" and cur_y != 5:
            if direction not in path[str(cur_x) + str(cur_y)]:
                path[str(cur_x) + str(cur_y)].add("U")
                path[str(cur_x) + str(cur_y + 1)].add("D")
                answer += 1
                # print(direction)
            cur_y += 1
        elif direction == "D" and cur_y != -5:
            if direction not in path[str(cur_x) + str(cur_y)]:
                path[str(cur_x) + str(cur_y)].add("D")
                path[str(cur_x) + str(cur_y - 1)].add("U")
                answer += 1
                # print(direction)
            cur_y -= 1
        elif direction == "R" and cur_x != 5:
            if direction not in path[str(cur_x) + str(cur_y)]:
                path[str(cur_x) + str(cur_y)].add("R")
                path[str(cur_x + 1) + str(cur_y)].add("L")
                answer += 1
                # print(direction)
            cur_x += 1
        elif direction == "L" and cur_x != -5:
            if direction not in path[str(cur_x) + str(cur_y)]:
                path[str(cur_x) + str(cur_y)].add("L")
                path[str(cur_x - 1) + str(cur_y)].add("R")
                answer += 1
                # print(direction)
            cur_x -= 1

    # print(path)
    return answer
