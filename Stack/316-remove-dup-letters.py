# https://leetcode.com/problems/remove-duplicate-letters/
from collections import defaultdict
from collections import Counter


# first idea -> make all
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        max_length = 0
        char_in = set()
        combination_dict = defaultdict(set)

        char_list = list(s)
        for c in char_list:
            if c in char_in:
                tmp_set = set(combination_dict[max_length])
                for item in combination_dict[max_length]:
                    tmp_set.add(item.replace(c, "") + c)
                combination_dict[max_length] = tmp_set
            else:
                max_length += 1
                char_in.add(c)
                if max_length == 1:
                    combination_dict[max_length].add(c)
                    continue

                for item in combination_dict[max_length - 1]:
                    combination_dict[max_length].add(item + c)

        print(combination_dict[max_length])
        return sorted(combination_dict[max_length])[0]

solution = Solution()
print(solution.removeDuplicateLetters("bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv"))


# using Stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # O(N)

        # char_count = Counter(s)
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1

        char_in = set()
        char_stack = list()
        char_list = list(s)
        # O(N) + O(N)
        for c in char_list:
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

solution = Solution()
print(solution.removeDuplicateLetters("bxshkpdwcsjdbikywvioxrypfzfbppydfilfxxtouzzjxaymjpmdoevv"))