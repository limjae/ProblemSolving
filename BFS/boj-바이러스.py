# https://www.acmicpc.net/problem/2606
from collections import defaultdict

nodes = int(input())
connections = int(input())

connect_dict = defaultdict(list)
is_infected = [-1 for _ in range(nodes + 1)]

for _ in range(connections):
    node1, node2 = input().split(" ")
    connect_dict[int(node1)].append(int(node2))
    connect_dict[int(node2)].append(int(node1))


def DFS(cur_node):
    infected = 1
    for connected_node in connect_dict[cur_node]:
        if is_infected[connected_node] == -1:
            is_infected[connected_node] = 1
            infected += DFS(connected_node)
    return infected


is_infected[1] = 1

print(DFS(1) - 1, end="")
