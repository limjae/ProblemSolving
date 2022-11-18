# https://school.programmers.co.kr/learn/courses/30/lessons/120875
def solution(dots):
    degree_set = set()

    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):
            print(i, j)
            dot1 = dots[i]
            dot2 = dots[j]

            x_degree = (dot1[0] - dot2[0])
            y_degree = (dot1[1] - dot2[1])
            degree = y_degree / x_degree if x_degree != 0 else 999999999
            if degree in degree_set:
                return 1
            degree_set.add(degree)

    return 0
