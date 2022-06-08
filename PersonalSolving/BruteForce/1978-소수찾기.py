# https://www.acmicpc.net/problem/1978
import math

import sys

input = sys.stdin.readline
num_count = int(input())
nums = list(map(int, input().split()))


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, math.ceil(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True


count = 0
for num in nums:
    if is_prime(num):
        count += 1

print(count, end="")
