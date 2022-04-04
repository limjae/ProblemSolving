import sys

input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    name, korean, english, math = input().split()
    list.append([name, int(korean), int(english), int(math)])

list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(list[i][0])