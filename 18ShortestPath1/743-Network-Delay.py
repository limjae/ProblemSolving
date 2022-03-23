# https://leetcode.com/problems/network-delay-time/
import copy
from typing import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        length_arr = [[999999 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            length_arr[i][i] = 0
        for info in times:
            length_arr[info[0]][info[1]] = info[2]

        connected = set()
        connected.add(k)
        length_result = copy.copy(length_arr[k])

        for _ in range(n-1):
            min_val = 999999
            min_index = -1

            for search_node in range(1, n+1):
                if search_node in connected:
                    continue
                elif length_result[search_node] < min_val:
                    min_val = length_result[search_node]
                    min_index = search_node

            if min_index == -1:
                return -1

            connected.add(min_index)
            for search_node in range(1, n+1):
                length_result[search_node] = min(length_result[search_node], length_result[min_index] + length_arr[min_index][search_node])

        return max(length_result[1:])



