class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            pivot = (start + end) // 2

            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                start = pivot + 1
            elif target < nums[pivot]:
                end = pivot - 1

        return start