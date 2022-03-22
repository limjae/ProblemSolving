# https://www.acmicpc.net/problem/2751
count = int(input())
answer = []
for _ in range(count):
    answer.append(int(input()))

answer.sort()
print("\n".join([str(i) for i in answer]), end="")