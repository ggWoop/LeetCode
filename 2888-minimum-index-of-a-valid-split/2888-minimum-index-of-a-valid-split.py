class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        from collections import Counter

        c1 = Counter()
        c1_cnt =0
        c2 = Counter(nums)
        c2_cnt =len(nums)
        dominant = c2.most_common()[0][0]


        for i in range(len(nums)):
            c1[nums[i]] += 1
            c1_cnt += 1
            c2[nums[i]] -= 1
            c2_cnt -= 1

            if c1[dominant] * 2 > c1_cnt and c2[dominant] * 2 > c2_cnt:
                return i
            
        return -1