# https://leetcode.com/problems/valid-anagram/submissions/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
