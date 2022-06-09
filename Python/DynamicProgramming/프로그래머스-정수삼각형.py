# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for y, row in enumerate(triangle[:-1]):
        for x, col in enumerate(row):
            dp[y+1][x] = max(dp[y+1][x], dp[y][x] + triangle[y+1][x])
            dp[y+1][x+1] = max(dp[y+1][x+1], dp[y][x] + triangle[y+1][x+1])

    return max(dp[len(dp)-1])
