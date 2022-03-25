import math

run = int(input())

for _ in range(run):
    start, end = list(map(int, input().split()))
    print(math.ceil(2 * math.sqrt(end - start)) - 1)