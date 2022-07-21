# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_count = [0 for _ in range(3)]

        for i in nums:
            color_count[i] += 1

        location = 0
        for i in range(3):
            for _ in range(color_count[i]):
                nums[location] = i
                location += 1

        return nums

