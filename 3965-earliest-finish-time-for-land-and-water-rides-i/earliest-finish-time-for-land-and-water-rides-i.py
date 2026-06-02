class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        

        n = len(landStartTime)
        m = len(waterStartTime)
        
        ans = float('inf')
        
        for i in range(n):

            land_finish = landStartTime[i] + landDuration[i] 

            for j in range(m):

                water_start = max(land_finish , waterStartTime[j])

                ans = min(ans , water_start + waterDuration[j])
        
        for j in range(m):

            water_finish = waterStartTime[j]  + waterDuration[j]

            for i in range(n):

                land_start = max(landStartTime[i] , water_finish)
                ans = min(ans , land_start + landDuration[i])
        return ans