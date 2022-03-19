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


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        answer = []
        for i in range(1, n+1, -1):
            stack.append([i])

        while stack:
            top = stack.pop
            if len(top) == k:
                answer.append(top)
                continue

            for i in range(top[-1] + 1 , n+1, -1):
                stack.append( top + [i] )

        return answer

