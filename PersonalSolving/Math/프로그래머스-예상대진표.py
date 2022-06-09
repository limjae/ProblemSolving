# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    ex = 0
    while n // 2 > 0:
        n = n // 2
        ex += 1

    cur = ex
    while (a - 1) // (2 ** cur) == (b - 1) // (2 ** cur) and cur > 0:
        print((a - 1) // (2 ** cur), (b - 1) // (2 ** cur))
        cur -= 1

    return cur + 1


