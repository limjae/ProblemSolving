# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    for i, count in enumerate(food):
        answer += str(i) * (count // 2)

    return answer + '0' + ''.join(reversed(answer))
