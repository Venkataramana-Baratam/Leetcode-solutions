class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        n = len(fruits)
        mpp = {}
        k = 2
        maxi = 0
        while r < n:
            if fruits[r] in mpp:
                mpp[fruits[r]] += 1
            else:
                mpp[fruits[r]] = 1

            if len(mpp.keys()) > k:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1

            if len(mpp.keys()) <= k:
                length = r - l + 1
                maxi = max(maxi, length)

            r += 1
        return maxi