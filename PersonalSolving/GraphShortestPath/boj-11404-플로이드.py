# https://www.acmicpc.net/problem/11404
import sys
from collections import defaultdict
input = sys.stdin.readline
graph = defaultdict(lambda: defaultdict(lambda: 9999999))

n = int(input())
edges = int(input())

for _ in range(edges):
    s, d, w = list(map(int, input().split()))
    graph[s-1][d-1] = min(graph[s-1][d-1], w)

distances = [[9999999 for _ in range(n)] for _ in range(n)]

for node_num in range(n):
    for node_dst in graph[node_num]:
        distances[node_num][node_dst] = graph[node_num][node_dst]
    distances[node_num][node_num] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
# floyd end

for index_y, row in enumerate(distances):
    for index_x, col in enumerate(row):
        if col == 9999999:
            distances[index_y][index_x] = "0"
        else:
            distances[index_y][index_x] = str(col)
    print(" ".join(row))