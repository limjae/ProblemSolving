# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    arr = rain_arr(k)
    for ran in ranges:
        start, l = ran
        end = len(arr) + l

        if end - start <= 0:
            answer.append(-1)
        else:
            size = 0
            for i in range(start, end - 1):
                size += (arr[i] + arr[i + 1]) / 2
            answer.append(size)
    return answer


def rain_arr(n):
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            arr.append(n // 2)
            n //= 2
        else:
            arr.append(n * 3 + 1)
            n = n * 3 + 1
    return arr
