class Solution:
    def finalString(self, s: str) -> str:

        answer = ""

        for i in range(len(s)):
            if s[i] == "i":
                answer= answer[::-1]
                continue
            answer += s[i]

        return answer 