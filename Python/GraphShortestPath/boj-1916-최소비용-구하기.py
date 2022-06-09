import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
graph = defaultdict(list)

n = int(input())
edges = int(input())

for _ in range(edges):
    s, d, w = list(map(int, input().split()))
    graph[s].append((d, w))

src, dst = list(map(int, input().split()))

pq = [(0, src)]

dist = defaultdict(lambda: 9999999)

while pq:
    distance, node = heapq.heappop(pq)
    if node not in dist:
        dist[node] = distance
        for v, w in graph[node]:
            alt = distance + w
            heapq.heappush(pq, (alt, v))

answer = []
for i in range(1, n+1):
    if dist[i] == 9999999:
        answer.append("INF")
    else:
        answer.append(str(dist[i]))

print(dist[dst], end="")
