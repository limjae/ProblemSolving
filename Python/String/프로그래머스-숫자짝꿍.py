# https://school.programmers.co.kr/learn/courses/30/lessons/131128
from collections import defaultdict


def solution(X, Y):
    answer = ''
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)
    common_dict = defaultdict(int)
    for x in X:
        x_dict[x] += 1

    for y in Y:
        y_dict[y] += 1

    for x in x_dict.keys():
        if min(x_dict[x], y_dict[x]) > 0:
            common_dict[x] = min(x_dict[x], y_dict[x])

    for c in common_dict.keys():
        for i in range(common_dict[c]):
            answer += c

    answer = sorted(answer, reverse=True)
    while len(answer) > 1 and answer[0] == '0':
        answer.pop(0)

    return "-1" if len(answer) == 0 else ''.join(answer)
