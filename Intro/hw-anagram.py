from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram 별로 모으는 Dict
        # anagram key :  word Array
        anagramGroup = {}

        for str in strs:
            key = "".join(sorted(str))
            if key not in anagramGroup:
                anagramGroup[key] = []
            anagramGroup[key].append(str)

        # 출력 순서는 관계없다 값만 존재하면 정답
        return anagramGroup.values()
