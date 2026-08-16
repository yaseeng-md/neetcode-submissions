from typing import List
from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
#         common_k = counter.most_common(k)
#         res = []
#         for ele, value in common_k:
#             res.append(ele)
#         return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for ele, frequency in counter.items():
            buckets[frequency].append(ele)
        results = []
        for idx in range(len(buckets)-1, 0, -1):
            for ele in buckets[idx]:
                results.append(ele)
            if len(results) >= k:
                return results
        
