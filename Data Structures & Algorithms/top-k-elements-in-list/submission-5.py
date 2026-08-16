from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        common_k = counter.most_common(k)
        res = []
        for ele, value in common_k:
            res.append(ele)
        return res