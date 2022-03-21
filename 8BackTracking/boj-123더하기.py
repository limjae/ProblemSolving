# https://www.acmicpc.net/problem/9095
numbers = int(input())
answer = []


def DFS(target_left):
    if target_left == 0:
        return 1

    count = 0
    for i in range(1, min(4, target_left + 1)):
        count += DFS(target_left - i)

    return count


for _ in range(numbers):
    target = int(input())
    answer.append(str(DFS(target)))

print("\n".join(answer), end="")
