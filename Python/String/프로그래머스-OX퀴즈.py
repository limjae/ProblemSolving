# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    for state in quiz:
        exp = state.split(" ")
        if exp[1] == "+":
            if int(exp[0]) + int(exp[2]) == int(exp[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(exp[0]) - int(exp[2]) == int(exp[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
