from collections import defaultdict
from collections import deque

n = int(input())
nodes = set([int(i) for i in range(n)])

child_dict = defaultdict(set)
parent_dict = defaultdict(int)
head = 0

input_tree = [int(i) for i in input().split(" ")]

for child, parent in enumerate(input_tree):
    if parent == -1:
        head = child
        continue
    else:
        child_dict[parent].add(child)
        parent_dict[child] = parent


target = int(input())
targets = deque([target])

if target == head:
    print(0, end="")
else:
    while targets:
        erase = targets.popleft()
        nodes.remove(erase)
        child_dict[parent_dict[erase]].remove(erase)
        for next_erase in child_dict[erase]:
            targets.append(next_erase)

    answer = 0
    for i in nodes:
        if not child_dict[i]:
            answer += 1
    print(answer, end="")