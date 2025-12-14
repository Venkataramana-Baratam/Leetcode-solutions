class Solution:
    def minMoves(self, balance: List[int]) -> int:
        
        if all(x>=0 for x in balance):
            return 0
        if sum(balance) < 0:
            return -1

        n = len(balance)
        neg_idx  = -1
        for i in range(n):
            if balance[i]<0:
                neg_idx = i
                break
        need = -balance[neg_idx]
        con = []
        for i in range(n):

            if i!=neg_idx and balance[i]>0:
                dist = min((i - neg_idx)%n,(neg_idx - i)%n)
                con.append((dist,balance[i]))
        min_moves = 0
        con.sort()
        for dist,amt in con:

            take = min(amt,need)
            min_moves+=take*dist
            need-=take
            if need == 0:
                return min_moves
        return -1