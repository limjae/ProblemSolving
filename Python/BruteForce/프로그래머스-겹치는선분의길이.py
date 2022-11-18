# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    answer = 0
    dup_set = set()
    lines.sort()
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            if line2[0] < min(line1[1], line2[1]):
                for k in range(line2[0], min(line1[1], line2[1])):
                    dup_set.add(k)

    return len(dup_set)
