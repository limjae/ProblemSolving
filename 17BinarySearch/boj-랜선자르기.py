# https://www.acmicpc.net/problem/1654
import sys

input = sys.stdin.readline

n, require = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)

while start <= end:
    cur = 0
    mid = (start + end) // 2
    for i in arr:
        cur += i // mid

    if cur < require:
        end = mid - 1
    else:
        start = mid + 1

    e = ('a' + 'b' +
         'c' + 'd')

print(end)
