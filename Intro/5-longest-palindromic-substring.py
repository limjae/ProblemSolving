from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        answer = s[0]
        # 홀수 substring case
        for i in range(len(s)-2):
            comp = self.longest_substring_from(i, i+2, s)
            answer = comp if len(answer) < len(comp) else answer
        # 짝수 substring case
        for i in range(len(s)-1):
            comp = self.longest_substring_from(i, i+1, s)
            answer = comp if len(answer) < len(comp) else answer

        return answer

    def longest_substring_from(self, start: int, end: int, s: str) -> str:

        while start >= 0 and end < len(s):
            # palindrome 평가
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break

        return s[start + 1: end]





