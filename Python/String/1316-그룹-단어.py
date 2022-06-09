import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
answer = 0
for _ in range(n):
    string = input()[:-1]
    char_dict = Counter(string)

    is_valid = True
    for char in char_dict:
        if string.rfind(char) - string.find(char) != char_dict[char] - 1:
            is_valid = False
            break

    if is_valid:
        answer += 1

print(answer)
