import sys

rounds = int(sys.stdin.readline())
for _ in range(rounds):
    target = int(sys.stdin.readline())
    if target == 0:
        print("1 0")
    elif target == 1:
        print("0 1")
    else:
        dp = [[0, 0] for _ in range(target + 1)]
        dp[0] = [1, 0]
        dp[1] = [0, 1]

        for i in range(2, target + 1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

        print(dp[target][0] , dp[target][1])
