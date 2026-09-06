from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        temp = 0
        result = 0

        for i in range(len(height)):

            if i < temp:
                continue

            if height[i] == 0:
                continue

            # --------------------------------
            # Find a right wall >= height[i]
            # --------------------------------

            j = i + 1

            while j < len(height) and height[j] < height[i]:
                j += 1

            # --------------------------------
            # CASE 1:
            # Found a wall >= left wall
            # --------------------------------

            if j < len(height):

                for k in range(i + 1, j):
                    result += height[i] - height[k]

                temp = j

            # --------------------------------
            # CASE 2:
            # No wall >= left wall
            # --------------------------------

            else:

                # Find the highest wall on the right
                max_height = 0
                max_index = -1

                for k in range(i + 1, len(height)):

                    if height[k] > max_height:
                        max_height = height[k]
                        max_index = k

                # No wall on the right
                if max_index == -1:
                    break

                # Calculate water using the smaller wall
                water_level = min(height[i], max_height)

                for k in range(i + 1, max_index):
                    result += water_level - height[k]

                temp = max_index

        return result