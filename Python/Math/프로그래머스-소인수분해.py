# https://school.programmers.co.kr/learn/courses/30/lessons/120852#

def solution(n):
    answer = set()
    for i in range(2, int(n ** (1 / 2)) + 2):
        if isPrime(i):
            while n % i == 0:
                answer.add(i)
                n //= i
    if n > 1:
        answer.add(n)

    return sorted(list(answer))


def isPrime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True
