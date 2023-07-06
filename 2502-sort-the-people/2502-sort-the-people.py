class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        tmp = []
        for name, height in zip(names,heights):
            tmp.append((name,height))
            sorted_arr = sorted(tmp, key=lambda x : x[1], reverse = True)
        return [name for name, height in sorted_arr]








