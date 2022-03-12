# https://www.acmicpc.net/problem/2164

from collections import deque
count = int(input())
answer = deque([i+1 for i in range(count)])

for i in range(count-1):
    answer.popleft()
    answer.append(answer.popleft())

print(answer.pop())

# 1 -> 1
# 2 -> 2
# 4 -> 4
# 6 -> 4
