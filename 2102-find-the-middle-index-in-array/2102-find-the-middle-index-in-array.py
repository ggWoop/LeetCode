class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l_cum_sum = []
        r_cum_sum = []
        l_prev = 0
        r_prev = 0
        for i in range(len(nums)):
            l_prev += nums[i]
            l_cum_sum.append(l_prev)
            r_prev += nums[len(nums)-1 -i]
            r_cum_sum = [r_prev] + r_cum_sum
        answer = -1

        for i in range(len(l_cum_sum)):
            if l_cum_sum[i] == r_cum_sum[i]:
                answer = i
                return answer

        return answer
  









