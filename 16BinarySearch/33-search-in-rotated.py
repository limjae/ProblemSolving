# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 미해결
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        start = 0
        end = nums_length-1

        while start <= end:
            mid = (start + end) // 2
            for i in arr:
                cur += max(i - mid, 0)

            if cur < limit:
                end = mid - 1
            else:
                start = mid + 1
