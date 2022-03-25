import sys
input_nums = int(sys.stdin.readline())
arr = [0]*10000
for _ in range(input_nums):
    arr[int(sys.stdin.readline())-1] += 1

for nums in range(10000):
    if arr[nums] > 0:
        for _ in range(arr[nums]):
            print(nums+1)


import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)