# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    extend_elements = elements + elements
    sum_set = set()

    for r in range(1, len(elements) + 1):
        for i in range(len(elements)):
            sum_set.add(sum(extend_elements[i:i + r]))

    answer = len(sum_set)
    return answer
