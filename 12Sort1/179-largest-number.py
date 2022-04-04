# https://leetcode.com/problems/largest-number/
import math
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = []
        for num in nums:
            sorted_nums.append([str(num) * (math.ceil(10 / len(str(num)))), len(str(num))])
        sorted_nums.sort(reverse=True)

        answer = "".join([s[:s_len] for s, s_len in sorted_nums])

        while len(answer) > 1 and answer[0] == "0":
            answer = answer[1:]

        return answer


