# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 미해결
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        start = 0
        end = nums_length-1

        while end - start > 1:
            mid = (start + end) // 2

            # start ~ mid까지 정렬
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            # mid ~ end까지 정렬
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        return end if target == nums[end] else start if target == nums[start] else -1

