class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        import numpy as np
        return sorted(np.array(nums) ** 2)