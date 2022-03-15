# https://www.acmicpc.net/problem/17219
count = input().split(" ")
password_count = int(count[0])
target_count = int(count[1])

password_dict = dict()
answer = list()

for _ in range(password_count):
    getInfo = input().split(" ")
    password_dict[getInfo[0]] = getInfo[1]

for _ in range(target_count):
    getInfo = input()
    answer.append(password_dict[getInfo])

print("\n".join(answer), end="")


