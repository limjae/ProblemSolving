from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            if i + max_length > len(s):
                break

            while max_length + 1 == len(set(list(s[i:i + max_length + 1]))):
                max_length += 1

        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(lambda: -1)
        left = 0
        max_length = 0
        for right, right_char in enumerate(s):
            if last_seen[right_char] < left:
                max_length = max(max_length, right - left + 1)
            else:
                left = last_seen[right_char] + 1
            last_seen[right_char] = right
        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))