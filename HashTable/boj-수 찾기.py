# https://www.acmicpc.net/problem/1920
count = int(input())

num_set = set()
answer = list()

getInfo = input().split(" ")

for s in getInfo:
    num_set.add(s)

# count가 필요한가?
count = int(input())
getInfo = input().split(" ")

for s in getInfo:
    if s in num_set:
        answer.append("1")
    else:
        answer.append("0")

print("\n".join(answer), end="")


