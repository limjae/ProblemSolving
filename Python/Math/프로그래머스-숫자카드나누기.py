# https://school.programmers.co.kr/learn/courses/30/lessons/135807
def solution(arrayA, arrayB):
    answer = 0

    return max(biggest_divisor(arrayA, arrayB), biggest_divisor(arrayB, arrayA))


def biggest_divisor(arrA, arrB):
    pivot_set = divisor_set(arrA[0])

    for i in list(pivot_set):
        for n1 in arrA:
            if n1 % i != 0:
                pivot_set.discard(i)

        for n2 in arrB:
            if n2 % i == 0:
                pivot_set.discard(i)

    return max(pivot_set) if len(pivot_set) > 0 else 0


def divisor_set(num):
    d_set = set()
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            d_set.add(i)
            d_set.add(num // i)
    return d_set
