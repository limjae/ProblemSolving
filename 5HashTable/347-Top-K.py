from collections import *
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict(Counter(nums))
        get_top_k = sorted(num_count.items(), key=lambda pair: pair[1], reverse=True)[:k]
        return [i[0] for i in get_top_k]
