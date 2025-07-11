class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                res.append(asteroids[i])
            else:
                while res and res[-1]>0 and res[-1]<abs(asteroids[i]):
                    res.pop()
                if res and res[-1]==abs(asteroids[i]):
                    res.pop()
                elif len(res)==0 or res[-1]<0:
                    res.append(asteroids[i])
        return res
