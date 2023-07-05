class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        answer = 1
        prev = 1
        for i in range(1, len(s)):
            diff = ord(s [i]) - ord(s [i - 1]) 
            print(diff)
            if diff == 1:
                prev += 1
                answer  = max(answer,prev)
            else:
                
                prev = 1
                answer  = max(answer,prev)
        return answer







