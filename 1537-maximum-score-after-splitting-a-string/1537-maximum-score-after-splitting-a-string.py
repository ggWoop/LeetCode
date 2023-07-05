class Solution:
    def maxScore(self, s: str) -> int:


        answer = 0

        for i in  range(1, len(s)):
            l = s[:i]
            r = s[i:]
            score = l.count("0") + r.count("1")
            answer = max(score, answer)
        return answer 






