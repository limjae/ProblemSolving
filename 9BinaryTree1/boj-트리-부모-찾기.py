from collections import defaultdict
from collections import deque

count = int(input())

connect_dict = defaultdict(list)
parent_dict = defaultdict(lambda: -1)
visit_deque = deque()
visit_deque.append(1)


for _ in range(count - 1):
    node1, node2 = [int(i) for i in input().split(" ")]
    connect_dict[node1].append(node2)
    connect_dict[node2].append(node1)

while visit_deque:
    cur_node = visit_deque.popleft()
    for compare_node in connect_dict[cur_node]:
        if parent_dict[compare_node] == -1:
            parent_dict[compare_node] = cur_node
            visit_deque.append(compare_node)


print("\n".join([str(parent_dict[i]) for i in range(2, count+1)]), end="")