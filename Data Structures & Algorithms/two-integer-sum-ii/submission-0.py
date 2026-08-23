from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            mid = (left + right) // 2
            ele_sum = numbers[left] + numbers[right]

            if ele_sum == target:
                return [left+1, right+1]

            elif ele_sum > target:
                right -= 1

            elif ele_sum < target:
                left += 1
        return []
