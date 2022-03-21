# https://www.acmicpc.net/problem/11650
count = int(input())
words = set()

for _ in range(count):
    words.add(input())

answer = list(words)
answer.sort(key=lambda x: (len(x), x))

print("\n".join(answer), end="")

