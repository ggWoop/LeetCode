class Solution:
    def balancedStringSplit(self, s: str) -> int:

        l_cum_sum = []
        r_cum_sum = []
        
        cur_l = 0
        cur_r = 0
        for c in s:

            if c == "R":
                cur_r += 1

            elif c == "L":
                cur_l += 1

            r_cum_sum.append(cur_r)
            l_cum_sum.append(cur_l)   

        answer = 0 

        for l_sum , r_sum in zip(l_cum_sum,r_cum_sum):
            if l_sum == r_sum:
                answer += 1
        return answer








