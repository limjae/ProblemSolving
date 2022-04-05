import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M, C = list(map(int, input().split()))
graph = defaultdict(set)
graph_reverse = defaultdict(set)

for _ in range(M):
    s, d, w = list(map(int, input().split()))
    graph[s-1].add((d-1, w))
    graph_reverse[d-1].add((s-1, w))

dist = [-1 for _ in range(N)]
dist_reverse = [-1 for _ in range(N)]
heap = [(0, C-1)]
heap_reverse = [(0, C-1)]


while heap:
    cur_dist, cur_index = heapq.heappop(heap)
    if dist[cur_index] == -1:
        dist[cur_index] = cur_dist
        for i, w in graph[cur_index]:
            if dist[i] == -1:
                heapq.heappush(heap, (cur_dist+w, i))


while heap_reverse:
    cur_dist, cur_index = heapq.heappop(heap_reverse)
    if dist_reverse[cur_index] == -1:
        dist_reverse[cur_index] = cur_dist
        for i, w in graph_reverse[cur_index]:
            if dist_reverse[i] == -1:
                heapq.heappush(heap_reverse, (cur_dist+w, i))

answer = 0
for i in range(N):
    answer = max(answer, dist[i] + dist_reverse[i])

print(answer)
