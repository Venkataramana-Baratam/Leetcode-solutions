class Solution:
    def countValidPrefixes(self, s: str) -> int:
        
        ans = 0

        i = 0 
        j = i

        while j < len(s):

            zeros = 0
            ones = 0

            for ch in s[i:j+1]:

                if ch == '0':
                    zeros+=1
                else:
                    ones+=1

            if abs(zeros - ones) <= 1:

                ans+=1

            j+=1
        return ans