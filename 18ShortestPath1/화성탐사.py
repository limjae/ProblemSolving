import sys
import heapq
input = sys.stdin.readline

rounds = int(input())

count = 1
for _ in range(rounds):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dist = [[9999999 for _ in range(n)] for _ in range(n)]
    # length, y, x
    pq = [(graph[0][0], 0, 0)]
    while pq:
        cur_dist, y, x = heapq.heappop(pq)
        if dist[y][x] == 9999999:
            dist[y][x] = cur_dist
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                new_y = y + dy[i]
                new_x = x + dx[i]
                if 0 <= new_y < n and 0 <= new_x < n and dist[new_y][new_x] == 9999999:
                    heapq.heappush(pq, (cur_dist + graph[new_y][new_x], new_y, new_x))


    print(f"Problem {count}: {dist[n-1][n-1]}")
    count += 1

