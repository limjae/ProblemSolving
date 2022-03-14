# https://leetcode.com/problems/permutations/
from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.DFS(nums, [])


    def DFS(self, input_list, return_list):
        if len(input_list) == 0:
            return [return_list]
        else:
            answer = []
            for index, digit in enumerate(input_list):
                tmp_list = list(input_list)
                tmp_input = tmp_list.pop(index)
                for word in self.DFS(tmp_list, list(return_list) + [tmp_input]):
                    answer.append(word)
            return answer


solution = Solution()
print(solution.permute([1, 2, 3]))