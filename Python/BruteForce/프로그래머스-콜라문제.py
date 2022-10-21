# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    while n >= a:
        payback = payback_cola(a,b,n)
        n = payback + n % a
        answer += payback

    return answer

def payback_cola(a, b, cur):
    return (cur//a) * b