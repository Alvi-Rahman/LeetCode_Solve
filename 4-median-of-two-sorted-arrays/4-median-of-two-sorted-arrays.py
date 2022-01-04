class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = sorted(nums1 + nums2)
        _len = len(sorted_array)
        flag = len(sorted_array) % 2
        return (sorted_array[int(_len/2)] + sorted_array[int(_len/2) - 1] ) / 2 if not                  flag else sorted_array[int(_len/2)]
    