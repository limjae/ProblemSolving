from heapq import *
length = int(input())
heap1 = []
answer = []

for _ in range(length):
    data = int(input())
    if data == 0:
        if heap1:
            answer.append(-heappop(heap1))
        else:
            answer.append(0)
    else:
        heappush(heap1, -data)
        
print("\n".join([str(i) for i in answer]), end="")