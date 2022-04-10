class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            pivot = start + (end - start) // 2

            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                start += 1
            else:
                end -= 1
        return -1