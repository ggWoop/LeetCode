class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        from collections import Counter

        # c1 = Counter()
        # c1_cnt =0
        # c2 = Counter(nums)
        # c2_cnt =0
        # dominant = c2.most_common()[0][0]


        # for i in range(len(nums)):
        #     c1[nums[i]] += 1
        #     c1_cnt += 1
        #     c2[nums[i]] += 1
        #     c2_cnt += 1

        #     if c1[dominant] * 2 > c1_cnt and c2[dominant] * 2 > c2_cnt:
        #         return i
            
        # return -1


        counter = Counter(nums)
        dominant = max(counter.keys(), key=counter.get)

        prefix = Counter()
        prefix_cnt = 0
        dominant_count = counter[dominant]

        for i, num in enumerate(nums):
            prefix[num] += 1
            prefix_cnt += 1
            counter[num] -= 1

            if counter[dominant] * 2 > len(nums) - prefix_cnt and prefix[dominant] * 2 > prefix_cnt:
                if i < len(nums) - 1:
                    return i

        return -1
