class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        remaining = numBottles
        while remaining>=numExchange:
            new_Bottles = remaining // numExchange
            total+=new_Bottles
            remaining = remaining % numExchange + new_Bottles
        return total