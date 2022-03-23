# https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1 for _ in range(n + 1)]

        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n]