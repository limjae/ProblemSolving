# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import defaultdict


def solution(array):
    answer = -1
    max_size = 0
    counter_map = defaultdict(int)

    for a in array:
        counter_map[a] += 1

    for key, value in counter_map.items():
        if max_size < value:
            answer = key
            max_size = value
        elif max_size == value:
            answer = -1

    return answer
