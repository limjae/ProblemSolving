from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # O(N)
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1

        string_list = [c for c in s]

        char_stack = list()
        for c in string_list:
            char_count[c] -= 1
            tmp_stack = list()
            tmp_stack.append(c)

            while char_stack:
                tmp = char_stack.pop()
                if tmp > c:
                    if char_count[tmp] == 0:
                        tmp_stack.append(tmp)
                elif tmp == c:
                    tmp_stack.append(tmp)
                    tmp_stack.pop(0)
                    break
                else:
                    tmp_stack.append(tmp)
                    break
            char_stack.append(tmp_stack.reverse())

        print("".join(char_stack))



