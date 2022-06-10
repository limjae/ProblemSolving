# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import defaultdict
from collections import deque


def solution(n, wires):
    answer = n

    connect_dict = defaultdict(set)
    child_net = [list() for _ in range(n)]
    node_set = set([i for i in range(1, n + 1)])

    for connection in wires:
        connect_dict[connection[1]].add(connection[0])
        connect_dict[connection[0]].add(connection[1])

    for connection in wires:
        left, right = connection[0], connection[1]
        connect_dict[connection[1]].remove(connection[0])
        connect_dict[connection[0]].remove(connection[1])

        left_set = set([left])
        right_set = set([right])

        queue = deque()
        queue.append(left)
        while queue:
            cur = queue.popleft()
            for next_node in connect_dict[cur]:
                if next_node not in left_set:
                    left_set.add(next_node)
                    queue.append(next_node)

        queue2 = deque()
        queue2.append(right)

        while queue2:
            cur = queue2.popleft()
            for next_node in connect_dict[cur]:
                if next_node not in right_set:
                    right_set.add(next_node)
                    queue2.append(next_node)

        answer = min(answer, abs(len(left_set) - len(right_set)))
        # print(left_set, right_set)

        connect_dict[connection[1]].add(connection[0])
        connect_dict[connection[0]].add(connection[1])

    return answer
