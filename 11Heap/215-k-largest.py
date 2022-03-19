# https://leetcode.com/problems/kth-largest-element-in-an-array/
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heappush(heap, n)

        for _ in range(k-1):
            heappop(heap)

        return heappop(heap)

