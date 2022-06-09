# https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    pre, cur = 0, 1

    for i in range(n):
        pre, cur = cur, (pre + cur) % 1234567
    return cur
