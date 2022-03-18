# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    runningWeight = 0
    truck_deque = deque(truck_weights)
    running = deque()

    while truck_deque or running:
        answer += 1

        for truck_stat in running:
            truck_stat[1] += 1

        if running:
            if running[0][1] == bridge_length:
                runningWeight -= running[0][0]
                running.popleft()

        if truck_deque:
            if runningWeight + truck_deque[0] <= weight:
                runningWeight += truck_deque[0]
                running.append([truck_deque.popleft(), 0])

    return answer

