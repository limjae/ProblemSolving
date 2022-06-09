# https://programmers.co.kr/learn/courses/30/lessons/12902
def solution(n):
    arr = [0 for _ in range(n+1)]
    if n > 0:
        arr[1] = 0
    if n > 1:
        arr[2] = 3
    if n > 2:
        arr[3] = 3
    if n > 3:
        arr[4] = 11
    if n > 4:
        arr[5] = 11
    for i in range(2, n-3):
        arr[i+4] = ( (arr[i+2] * 4) % 1000000007 - arr[i] % 1000000007 + 1000000007) % 1000000007
    return arr[n]