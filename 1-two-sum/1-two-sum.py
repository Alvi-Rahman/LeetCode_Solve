class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in _dict:
                return [i, _dict[complement]]
            _dict[nums[i]] = i