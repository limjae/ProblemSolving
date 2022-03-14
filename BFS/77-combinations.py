from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       return self.DFS(k, n, [])

    def DFS(self, left, n, result):
        if left == 0:
            return [ result ]
        else:
            answer = []
            top = result[-1] if result else 0
            for i in range(top + 1, n + 1):
                answer += self.DFS(left - 1, n+1, list(result) + [i])
            return answer

