# https://school.programmers.co.kr/learn/courses/30/lessons/120923
from collections import deque


def solution(num, total):
    answer = deque([])
    n = total // num
    cur_total = 0
    for i in range(n, n + num):
        answer.append(i)
        cur_total += i

    while cur_total != total:
        if cur_total < total:
            nxt = answer[num - 1] + 1
            cur_total -= answer.popleft()
            answer.append(nxt)
            cur_total += nxt
        elif cur_total > total:
            nxt = answer[0] - 1
            cur_total -= answer.pop()
            answer.appendleft(nxt)
            cur_total += nxt

    return list(answer)
