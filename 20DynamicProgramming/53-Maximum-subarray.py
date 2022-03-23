# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0 for _ in range(len(nums))]
        answer = nums[0]
        arr[0] = nums[0]
        for index in range(1, len(nums)):
            if arr[index-1] < 0:
                arr[index] = nums[index]
            else:
                arr[index] = arr[index-1] + nums[index]
            answer = max(answer, arr[index])
        return answer