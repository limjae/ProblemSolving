from collections import *
from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]

        temp_stack = list()
        for cur_index, cur_temp in enumerate(temperatures):
            while temp_stack:
                index = temp_stack.pop()
                if temperatures[index] < cur_temp:
                    answer[index] = cur_index - index
                else:
                    temp_stack.append(index)
                    break

            temp_stack.append(cur_index)

        return answer
