# https://school.programmers.co.kr/learn/courses/30/lessons/120863#
def solution(polynomial):
    x_count = 0
    count = 0

    state = polynomial.split(" ")

    for s in state:
        if s == "+":
            continue
        if s == "*":
            continue

        if s[len(s) - 1] == "x":
            x_count += int(s[:len(s) - 1]) if len(s) > 1 else 1
        else:
            count += int(s)

    if x_count == 0:
        return str(count)
    elif count == 0:
        return str(x_count) + "x" if x_count != 1 else "x"
    return str(x_count) + "x + " + str(count) if x_count != 1 else "" + "x + " + str(count)
