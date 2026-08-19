from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right_ptr = len(heights)-1
        left_ptr = 0
        max_area = 0
        while left_ptr <= right_ptr:
            # print(left_ptr, right_ptr)
            left = heights[left_ptr]
            right = heights[right_ptr]

            lenght = min(left, right)
            breadth = right_ptr - left_ptr
            # print(lenght, breadth)
            area = lenght * breadth
            max_area = max(max_area, area)

            if left < right:
                left_ptr += 1
            elif right < left:
                right_ptr -= 1
            elif right == left:
                left_ptr += 1
                right_ptr -= 1
            # print(left_ptr, right_ptr)
            
        return max_area
