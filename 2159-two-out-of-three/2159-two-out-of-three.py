class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        
        # 각 집합에서 다른 두 집합과의 교집합을 찾고, 이 교집합들을 합침
        return list((set1 & set2) | (set2 & set3) | (set1 & set3))




