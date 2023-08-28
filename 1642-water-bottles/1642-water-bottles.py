class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        answer = 0


        while numBottles >= numExchange:

            exchange = numBottles // numExchange
            drink = exchange * numExchange
            answer += drink
            numBottles =numBottles - drink + exchange
        answer += numBottles



        return answer
