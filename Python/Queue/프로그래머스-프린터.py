from collections import deque


def solution(priorities, location):
    sequence = 0
    queue = deque()

    for i, val in enumerate(priorities):
        queue.append([i, val])

    while queue:
        cur = queue.popleft()
        cur_location, cur_value = cur[0], cur[1]

        if queue and max(list(zip(*queue))[1]) > cur_value:
            queue.append([cur_location, cur_value])
        else:
            sequence += 1
            if cur_location == location:
                return sequence

    return sequence
