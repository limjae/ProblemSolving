from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phonedict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        answer = [""]

        for num in digits:
            tmp = []

            for combination in answer:
                for char in phonedict[num]:
                    tmp.append(combination + char)

            answer = tmp

        return answer

solution = Solution()
print(solution.letterCombinations("23"))


class Solution:
    phonedict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }


    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if digits == "":
            return answer
        else:
            stack = list(digits)
            answer += self.DFS(list(stack), "")
        return answer

    def DFS(self, stack, string):
        digit = stack.pop()
        if len(stack) == 0:
            return [c + string for c in self.phonedict[digit]]
        else:
            answer = []
            for c in list(self.phonedict[digit]):
                answer += self.DFS(list(stack), c + string)
            return answer


solution = Solution()
print(solution.letterCombinations("23"))

