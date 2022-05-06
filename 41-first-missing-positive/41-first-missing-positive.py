class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter = 1
        s = set(nums)
        while True:
            if counter not in s:
                return counter
            counter += 1