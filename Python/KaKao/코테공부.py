def solution(alp, cop, problems):
    answer = 0

    target_alp = alp
    target_cop = cop
    target_increment = 1

    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        target_alp = max(target_alp, alp_req)
        target_cop = max(target_cop, cop_req)
        target_increment = max(alp_rwd, cop_rwd, target_increment)

    dp = [[999 for _ in range(151 + target_increment)] for _ in range(151 + target_increment)]
    dp[alp][cop] = 0
    #     dynamic
    for alp_index in range(alp, target_alp+1):
        for cop_index in range(cop, target_cop+1):
            dp[alp_index][cop_index + 1] = min(dp[alp_index][cop_index + 1], dp[alp_index][cop_index] + 1)
            dp[alp_index + 1][cop_index] = min(dp[alp_index + 1][cop_index], dp[alp_index][cop_index] + 1)

            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_index >= alp_req and cop_index >= cop_req:
                    next_alp,next_cop = min(target_alp,alp_index + alp_rwd), min(target_cop,cop_index + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[alp_index][cop_index] + cost)


    #         slice = [dp[i][cop:target_cop+1] for i in range(alp, target_alp+1)]
    #         for s in slice:
    #             print(s)

    slice = [dp[i][cop:target_cop+1] for i in range(alp, target_alp+1)]
    for s in slice:
        print(s)
    print(dp[target_alp][target_cop])

    return dp[target_alp][target_cop]