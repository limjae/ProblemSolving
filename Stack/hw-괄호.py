count = int(input())
answer = ["YES" for _ in range(count)]

for i in range(count):
    s = input()

    char_list = [c for c in s]
    stack = list()

    for c in char_list:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                answer[i] = "NO"
            elif stack.pop() != '(':
                answer[i] = "NO"
    if stack:
        answer[i] = "NO"

print("\n".join(answer), end='')


# 4
# (())
# ()()
# ((((
# ))))
# YES
# YES
# NO
# NO
