# https://www.acmicpc.net/problem/11650
count = int(input())
points = []

for _ in range(count):
    points.append([int(i) for i in input().split(" ")])

points.sort(key=lambda x: (x[1], x[0]))
parse = [str(pt[0])+" "+str(pt[1]) for pt in points]

print("\n".join(parse), end="")

