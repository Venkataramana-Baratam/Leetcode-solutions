class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(X, Y):
            m, n = len(X), len(Y)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if X[i - 1] == Y[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            i, j = m, n
            lcs_str = []
            while i > 0 and j > 0:
                if X[i - 1] == Y[j - 1]:
                    lcs_str.append(X[i - 1])
                    i -= 1
                    j -= 1
                elif dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1
            return ''.join(reversed(lcs_str))
        
        lcs_str = lcs(str1, str2)
        i = j = 0
        result = []
        
        for c in lcs_str:
            while i < len(str1) and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1
        
        result.append(str1[i:])
        result.append(str2[j:])
        
        return ''.join(result)
