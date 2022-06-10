# https://programmers.co.kr/learn/courses/30/lessons/76503
from collections import defaultdict

def solution(a, edges):
    answer = 0

    if sum(a) != 0:
        return -1

    connect_dict = defaultdict(set)
    for connection in edges:
        connect_dict[connection[0]].add(connection[1])
        connect_dict[connection[1]].add(connection[0])

    tree_stack = list()
    tree_set = set()
    tree_par = [-1 for _ in a]

    tree_stack.append(0)
    tree_set.add(0)


    for i in range(len(a)):
        cur = tree_stack[i]
        for next_node in connect_dict[cur]:
            if next_node not in tree_set:
                tree_stack.append(next_node)
                tree_set.add(next_node)
                tree_par[next_node] = cur

    while tree_stack:
        cur = tree_stack.pop()
        if tree_par[cur] == -1:
            return answer
        a[tree_par[cur]] += a[cur]
        answer += abs(a[cur])

