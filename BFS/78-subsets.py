from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        nums_index = {}

        for index, num in enumerate(nums):
            nums_index[num] = index

        subsets = [[] for _ in range(nums_length + 1)]
        subsets[0].append([])

        for i in range(nums_length + 1):
            for subset in subsets[i - 1]:
                last_item_index = nums_index[subset[-1]] if subset else -1

                for num_index in range(last_item_index + 1, nums_length):
                    subsets[i].append(subset + [nums[num_index]])

        answer = []
        for i in range(nums_length + 1):
            answer += subsets[i]

        return answer