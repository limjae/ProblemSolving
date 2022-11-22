# https://school.programmers.co.kr/learn/courses/30/lessons/131704
def solution(order):
    answer = 0
    req = list(reversed(order))
    sub_stack = []

    cur = 1
    while req:
        target = req[-1]
        if target == cur:
            answer += 1
            cur += 1
            req.pop()
        elif target > cur:
            sub_stack.append(cur)
            cur += 1
        elif sub_stack and target == sub_stack[-1]:
            answer += 1
            sub_stack.pop()
            req.pop()
        else:
            break

    return answer
