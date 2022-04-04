import sys
n_student = int(sys.stdin.readline())
arr = []
for _ in range(n_student):
    name, score = sys.stdin.readline().split()
    arr.append([int(score), name])

arr.sort()
for a in arr:
    print(a[1], end=" ")


