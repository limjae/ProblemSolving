import sys
input = sys.stdin.readline

length = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
answer = 0
for a in range(length):
    cur_val = 0
    for i in range(length):
        cur_val += arr1[(i+a) % length] * arr2[i]

    answer = max(cur_val, answer)

print(answer)