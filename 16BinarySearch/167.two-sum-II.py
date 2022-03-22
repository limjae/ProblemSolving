# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        while not lp == rp:
            if numbers[lp] + numbers[rp] > target:
                return lp+1, rp+1
            elif numbers[lp] + numbers[rp] < target:
                lp += 1
            else:
                rp -= 1