class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums, n = [1] + nums + [1], len(nums) + 2 
        lst = [[0] * n for _ in range(n)] 
        
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                lst[left][right] = max(nums[left]*nums[i]*nums[right] + lst[left][i] + lst[i]                                       [right] for i in range(left + 1, right))
        
        return lst[0][n-1]