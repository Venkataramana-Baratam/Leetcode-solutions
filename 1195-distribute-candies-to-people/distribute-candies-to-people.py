class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        res  = [0] * num_people

        give = 1
        i = 0
        while candies>0:

            if candies>=give:

                res[i]+=give
                candies-=give
            else:

                res[i] += candies
                break

            give+=1
            i = (i+1)%num_people
        return res