# https://www.acmicpc.net/problem/5052
rounds = int(input())
answer = []
for _ in range(rounds):
    nums = int(input())
    arr = []
    for _ in range(nums):
        arr.append(input())

    arr.sort()

    print(arr)
    valid = True
    for index in range(nums - 1):
        if arr[index + 1].find(arr[index]) == 0:
            valid = False
            break

    if valid:
        answer.append("YES")
    else:
        answer.append("NO")

print("\n".join(answer), end="")