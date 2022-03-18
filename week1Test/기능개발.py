# https://programmers.co.kr/learn/courses/30/lessons/42586
from math import ceil

def solution(progresses, speeds):
    answer = []
    end_stack = []

    while progresses:
        end_stack.append(ceil((100 - progresses.pop()) / speeds.pop()))

    while end_stack:
        pivot = end_stack.pop()
        count = 1
        while end_stack and end_stack[-1] <= pivot:
            count += 1
            end_stack.pop()
        answer.append(count)

    return answer