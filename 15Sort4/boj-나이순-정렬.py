# https://www.acmicpc.net/problem/10814
count = int(input())
ages = []

for _ in range(count):
    age, name = input().split(" ")
    ages.append([int(age), name])

ages.sort(key=lambda x: (x[0]))
answer = [str(age)+" "+name for age, name in ages]
print("\n".join(answer), end="")