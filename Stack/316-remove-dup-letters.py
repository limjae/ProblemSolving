# https://leetcode.com/problems/remove-duplicate-letters/
from collections import defaultdict
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # O(N)
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1

        char_in = defaultdict(lambda: False)
        char_stack = list()
        string_list = [c for c in s]
        for c in string_list:
            char_count[c] -= 1

            if char_in[c]:
                continue

            while char_stack:
                if char_stack[-1] < c:
                    break
                elif char_count[char_stack[-1]] == 0:
                    break
                else:
                    char_in[char_stack[-1]] = False
                    char_stack.pop()

            char_in[c] = True
            char_stack.append(c)

        return "".join(char_stack)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # O(N)
        # char_count = Counter(s)
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1

        char_in = set()
        char_stack = list()
        string_list = [c for c in s]
        for c in string_list:
            char_count[c] -= 1

            if c in char_in:
                continue

            while char_stack:
                if char_stack[-1] < c:
                    break
                elif char_count[char_stack[-1]] == 0:
                    break
                else:
                    out = char_stack.pop()
                    char_in.remove(out)

            char_in.add(c)
            char_stack.append(c)

        return "".join(char_stack)
