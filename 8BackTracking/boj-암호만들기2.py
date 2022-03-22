import sys
import itertools

input = sys.stdin.readline

l, c = map(int, input().split())
# input 값을 사전식으로 정렬
wordList = sorted(list(input().split()))

# l개의 경우를 모두 뽑아주고 특정 조건(모음 1개이상, 자음 2개 이상)을 만족하는 값만 보여주면 된다.
vowel = ["a", "e", "i", "o", "u"]

for i in wordList:
    result = list(itertools.combinations(wordList, l))

answer = []
for res in result:
    v_count = 0
    c_count = 0
    for c in res:
        if c in vowel:
            v_count += 1
        else:
            c_count += 1
    if v_count > 0 and c_count > 1:
        answer.append(res)

print("\n".join(["".join(s) for s in answer]), end="")



