from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        longest = 1
        temp = 1
        first = nums[0]
        for ele in nums[1:]:
            if first + 1 == ele:
                temp += 1
            else:
                if longest < temp:
                    longest = temp
                temp = 1
            
            first = ele

        if temp > longest:
            longest = temp

        return longest