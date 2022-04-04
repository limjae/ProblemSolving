# https://www.acmicpc.net/problem/2805
import sys

input = sys.stdin.readline

n, limit= list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    cur = 0
    mid = (start + end) // 2
    for i in arr:
        cur += max(i - mid, 0)

    if cur < limit:
        end = mid - 1
    else:
        start = mid + 1

print(end)
