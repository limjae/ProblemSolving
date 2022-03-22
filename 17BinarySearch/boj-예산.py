import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
limit = int(input())

start = 0
end = max(arr)

while start <= end:
    cur = 0
    mid = (start + end) // 2
    for i in arr:
        cur += min(mid, i)

    if cur <= limit:
        start = mid + 1
    else:
        end = mid - 1

print(end)