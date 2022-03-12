from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(len(nums) - 1, -1, -2):
            answer += nums[i]

        return answer