from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_count = defaultdict(int)

        for c in stones:
            stones_count[c] += 1

        count = 0
        for c in jewels:
            count += stones_count[c]

        return count
