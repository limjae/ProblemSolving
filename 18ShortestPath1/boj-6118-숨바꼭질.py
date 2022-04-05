import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
v, e = list(map(int, input().split()))

graph = defaultdict(set)
for _ in range(e):
    from_v, to_v = list(map(int, input().split()))
    graph[from_v-1].add(to_v-1)
    graph[to_v-1].add(from_v-1)


dist = [-1 for _ in range(v)]
heap = [(0, 0)]

while heap:
    cur_dist, cur_index = heapq.heappop(heap)
    if dist[cur_index] == -1:
        dist[cur_index] = cur_dist
        for i in graph[cur_index]:
            if dist[i] == -1:
                heapq.heappush(heap, (cur_dist+1, i))

mx = max(dist)
print(dist.index(mx)+1, mx, dist.count(mx))