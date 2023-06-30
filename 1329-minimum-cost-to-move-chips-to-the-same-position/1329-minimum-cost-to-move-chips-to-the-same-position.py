class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:


        # one = position.count(1)
        # two = position.count(2)
        # three = position.count(3)

        # max_num = max(one, two, three)

        

        # for i in range(len(position)):

        nOdd, nEven = 0, 0
        for i in position:
            if i % 2 == 0:
                nEven += 1
            else:
                nOdd += 1
        return min(nEven, nOdd)





