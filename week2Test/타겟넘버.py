# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
from collections import deque
def solution(numbers, target):
    length = len(numbers)
    answer = 0
    bfs_queue = deque()
    bfs_queue.append((0, 0))

    while bfs_queue:
        value, index = bfs_queue.popleft()

        if index == length:
            if value == target:
                answer += 1
            else:
                continue
        else:
            bfs_queue.append((value + numbers[index], index + 1))
            bfs_queue.append((value - numbers[index], index + 1))


    return answer