# https://www.acmicpc.net/problem/1966
from collections import deque
count = int(input())
answer = []

for i in range(count):
    getInfo = input().split(" ")
    docs, target = int(getInfo[0]), int(getInfo[1])

    index_queue = deque([info for info in range(docs)])
    getInfo = input().split(" ")
    priority_list = [int(info) for info in getInfo]

    count = 1
    while index_queue:
        is_prior = True
        for it, index in enumerate(index_queue, start=1):
            if priority_list[index_queue[0]] < priority_list[index]:
                is_prior = False
                break

        if is_prior:
            if index_queue[0] == target:
                break
            else:
                index_queue.popleft()
                count += 1
        else:
            index_queue.append(index_queue.popleft())

    answer.append(str(count))


print("\n".join(answer), end="")

