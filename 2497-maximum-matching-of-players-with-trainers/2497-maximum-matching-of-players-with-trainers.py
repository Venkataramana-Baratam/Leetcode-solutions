from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        total = 0
        j = 0

        for i in range(len(players)):
            while j < len(trainers):
                if players[i] <= trainers[j]:
                    total += 1
                    j += 1  
                    break
                j += 1  
        return total
