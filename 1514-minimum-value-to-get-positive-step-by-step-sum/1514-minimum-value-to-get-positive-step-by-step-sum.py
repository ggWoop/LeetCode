class Solution:
    def minStartValue(self, nums: List[int]) -> int:

            cum_sum = []
            prev = 0
            for num in nums:
                prev += num
                cum_sum.append(prev)

            min_val = min(cum_sum)
            if min_val >0:
                return 1
            return -min_val +1






















