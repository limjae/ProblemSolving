import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = []
    pq = []
    visited = [False for _ in range(n+1)]
    path_graph = defaultdict(list)
    min_intensity = -1

    for path in paths:
        fr, to, inten = path
        path_graph[fr].append([to, inten])
        path_graph[to].append([fr, inten])

    for gate in gates:
        heapq.heappush(pq, [0, gate])

    while pq:
        cur_intensity, cur_node = heapq.heappop(pq)

        if visited[cur_node] == False:
            visited[cur_node] = True


            if cur_node in summits:
                if min_intensity > 0:
                    if min_intensity < cur_intensity:
                        return answer
                    elif answer[0] > cur_node:
                        print(answer)
                        answer[0] = cur_node
                else:
                    min_intensity = cur_intensity
                    answer = [cur_node, cur_intensity]
                    print(answer)
            else:
                for path in path_graph[cur_node]:
                    to, next_intensity = path
                    heapq.heappush(pq, [max(cur_intensity, next_intensity), to])


    return answer