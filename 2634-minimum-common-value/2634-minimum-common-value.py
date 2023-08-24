class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_elements = list(set(nums1) & set(nums2))
        if common_elements:
            return min(common_elements)
        else:
            return -1  # 또는 다른 적절한 정수 값을 반환합니다.



