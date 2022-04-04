from collections import defaultdict

def solution(N, stages):
    fail_amount = defaultdict(int)
    reach_amount = defaultdict(int)

    for i in stages :
        fail_amount[i] += 1
        reach_amount[i] += 1

    for i in range(N+1, 1, -1):# N+1 ~ 2 range
        reach_amount[i-1] += reach_amount[i]

    print(reach_amount, fail_amount)

    fail_rank = [[i, fail_amount[i]/reach_amount[i] if reach_amount[i] != 0 else 0] for i in range(1, N+1)]
    print(fail_rank)
    fail_rank.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in fail_rank]