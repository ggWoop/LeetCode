class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        answer = -1
        n = len(words)
        for i in range(len(words)):
            l = words[(startIndex - i) % n]
            r = words[(startIndex + i) % n]
            if target == l or target == r:
                return i

        return answer