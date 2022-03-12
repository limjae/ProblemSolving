import string

S = input()
output = {}

for lo in string.ascii_lowercase:
    output.append(str(S.find(lo)))

def get_idx(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    key = ' '.join([str(num) for num in result])
    if(not key in output):
        output[key] = []

    output[key].append(word)


answer = " ".join(output)
print(answer)