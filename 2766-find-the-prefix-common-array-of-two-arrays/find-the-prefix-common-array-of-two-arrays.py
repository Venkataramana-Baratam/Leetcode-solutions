class Solution:
    def findThePrefixCommonArray(self, A, B):

        seen = {}
        res = []

        common = 0

        for i in range(len(A)):

           
            seen[A[i]] = seen.get(A[i], 0) + 1

            if seen[A[i]] == 2:
                common += 1

            
            seen[B[i]] = seen.get(B[i], 0) + 1

            if seen[B[i]] == 2:
                common += 1

            res.append(common)

        return res