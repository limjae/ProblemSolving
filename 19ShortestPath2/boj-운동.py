# https://www.acmicpc.net/problem/1956
import sys
from collections import defaultdict
input = sys.stdin.readline
graph = defaultdict(list)

n, edges = list(map(int, input().split()))

for _ in range(edges):
    s, d, w = list(map(int, input().split()))
    graph[s-1].append((d-1, w))

distances = [[9999999 for _ in range(n)] for _ in range(n)]

for node_num in range(n):
    for edge in graph[node_num]:
        distances[node_num][edge[0]] = edge[1]
    distances[node_num][node_num] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
# floyd end


min_distance = 9999999
for start in range(n):
    for via in range(n):
        if start == via:
            continue
        min_distance = min(min_distance, distances[start][via] + distances[via][start])

print(-1 if min_distance == 9999999 else min_distance, end="")
