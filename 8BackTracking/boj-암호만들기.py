# https://www.acmicpc.net/problem/1759
length, types = [int(i) for i in input().split(" ")]
letters = sorted(input().split(" "))
vowels = "aeiou"
letters_index = {}
for index, char in enumerate(letters):
    letters_index[char] = index

answer = []

def DFS(cur_string):
    if len(cur_string) == length:
        vowel = 0
        not_vowel = 0
        for c in cur_string:
            if c in vowels:
                vowel += 1
            else:
                not_vowel += 1

        if vowel > 0 and not_vowel > 1:
            answer.append(cur_string)
        return None

    for i in range(max(0, letters_index[cur_string[-1]] + 1), types):
        DFS(cur_string + letters[i])

    return None


for i in range(0, types):
    DFS(letters[i])

print("\n".join(answer), end="")

