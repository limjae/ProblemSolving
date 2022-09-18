def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    cost_from_s = [INF] * (n + 1)
    cost_from_a = [INF] * (n + 1)
    cost_from_b = [INF] * (n + 1)
    cost_from_s[s] = 0
    cost_from_a[a] = 0
    cost_from_b[b] = 0

    for i in range(n + 1):
        for x, y, cost in fares:
            cost_from_s[y] = min(cost_from_s[y], cost_from_s[x] + cost)
            cost_from_s[x] = min(cost_from_s[x], cost_from_s[y] + cost)

            cost_from_a[y] = min(cost_from_a[y], cost_from_a[x] + cost)
            cost_from_a[x] = min(cost_from_a[x], cost_from_a[y] + cost)

            cost_from_b[y] = min(cost_from_b[y], cost_from_b[x] + cost)
            cost_from_b[x] = min(cost_from_b[x], cost_from_b[y] + cost)

    # print(cost_from_s)
    # print(cost_from_a)
    # print(cost_from_b)
    for i in range(1, n + 1):
        answer = min(answer, cost_from_s[i] + cost_from_a[i] + cost_from_b[i])

    return answer
