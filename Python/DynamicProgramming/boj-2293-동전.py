# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline

n, target = list(map(int, input().split()))
c = [int(input()) for _ in range(n)]
max_coin = max(c)

dp = [0 for _ in range(target+1)]
dp[0] = 1

for coin_index, coin in enumerate(c):
    for i in range(coin, target + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[target] if dp[target] != 0 else -1, end="")

