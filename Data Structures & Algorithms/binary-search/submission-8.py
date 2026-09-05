class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while left_idx <= right_idx:
        
            mid = (left_idx + right_idx) // 2
            print(mid, left_idx, right_idx)

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left_idx = mid + 1
            elif nums[mid] > target:
                right_idx = mid - 1

        return -1
