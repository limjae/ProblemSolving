# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        len_d = count_divisor(i)
        steel = len_d if len_d <= limit else power
        answer += steel

    return answer


def count_divisor(num):
    divisor_set = set()
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            divisor_set.add(i)
            divisor_set.add(num // i)
    return len(divisor_set)
