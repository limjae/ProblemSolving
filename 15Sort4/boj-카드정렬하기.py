import sys
import heapq
input = sys.stdin.readline

card_num = int(input())
card_heap = list()
for i in range(card_num):
    heapq.heappush(card_heap, int(input()))

answer = 0
while len(card_heap) > 1:
    a = heapq.heappop(card_heap)
    b = heapq.heappop(card_heap)
    heapq.heappush(card_heap, a+b)
    answer += a + b

print(answer)