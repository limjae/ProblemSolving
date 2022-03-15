from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 3 point
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while right > left:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
                elif total < 0:
                    left += 1
                    while nums[left] == nums[left - 1] and right > left:
                        left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and right > left:
                        left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
        return results


