# https://www.acmicpc.net/problem/11727
import sys
input = sys.stdin.readline

target = int(input())

dp = [0 for _ in range(target+1)]
dp[0] = 1
dp[1] = 1

for i in range(2, target + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[target], end="")

