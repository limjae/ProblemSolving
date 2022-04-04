import math
def solution(n, times):
    left = max(times) * n // len(times)
    right = max(times) * math.ceil(n / len(times))
    print(left, right)
    return answer