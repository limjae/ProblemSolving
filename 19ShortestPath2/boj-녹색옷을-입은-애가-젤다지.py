# https://www.acmicpc.net/problem/4485
import sys
import heapq
input = sys.stdin.readline

n = int(input())
count = 1
while n != 0:
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

            if y > 0 and dist[y-1][x] == 9999999:
                heapq.heappush(pq, (cur_dist + graph[y-1][x], y-1, x))
            if x > 0 and dist[y][x-1] == 9999999:
                heapq.heappush(pq, (cur_dist + graph[y][x-1], y, x-1))
            if y < n-1 and dist[y+1][x] == 9999999:
                heapq.heappush(pq, (cur_dist + graph[y+1][x], y+1, x))
            if x < n-1 and dist[y][x+1] == 9999999:
                heapq.heappush(pq, (cur_dist + graph[y][x+1], y, x+1))

    print(f"Problem {count}: {dist[n-1][n-1]}")
    count += 1
    # print(dist)

    n = int(input())


