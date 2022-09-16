from collections import defaultdict


def solution(info, edges):
    answer = 0
    tree = defaultdict(list)

    for edge in edges:
        tree[edge[0]].append(edge[1])

    def DFS(cur, cur_sheeps, cur_wolves, visited, available):
        next_sheep = cur_sheeps
        next_wolves = cur_wolves
        if info[cur] == 0:
            next_sheep += 1
        else:
            next_wolves += 1

        if next_sheep <= next_wolves:
            return [cur_sheeps, cur_wolves, list(visited), set(available)]
        else:
            next_visted = list(visited)
            next_visted.append(cur)
            next_available = set(available)
            for nxt in tree[cur]:
                next_available.add(nxt)

            max_sheep = [[next_sheep, next_wolves, next_visted]]

            for nxt in next_available:
                if nxt not in next_visted:
                    case = DFS(nxt, next_sheep, next_wolves, next_visted, next_available)
                    max_sheep.append(case)

            max_sheep.sort(key=lambda x: (x[0], -x[1]))
            return max_sheep.pop()

    return DFS(0, 0, 0, [], {0})[0]
