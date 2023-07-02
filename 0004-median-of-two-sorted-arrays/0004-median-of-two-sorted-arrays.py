class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        
        sorted_nums = sorted(nums1+ nums2)
        #print(sorted_nums)

        

        return np.median(sorted_nums)
