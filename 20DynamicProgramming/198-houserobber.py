# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        rob_max = [0 for _ in range(length)]

        if length > 0:
            rob_max[0] = nums[0]
        if length > 1:
            rob_max[1] = max(nums[1], nums[0])

        for i in range(2, length):
            rob_max[i] = max(rob_max[i - 1], rob_max[i - 2] + nums[i])

        return rob_max[-1]