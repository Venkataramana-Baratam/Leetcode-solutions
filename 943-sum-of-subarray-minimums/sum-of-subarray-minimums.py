class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        

        n = len(arr)
        def findnse(arr):

            st = []

            nse = [n]*n

            for i in range(n-1,-1,-1):

                while st and arr[st[-1]]>=arr[i]:
                    st.pop()

                nse[i] = st[-1] if st else n

                st.append(i)

            return nse

        def findpsee(arr):

            pse = [-1]*n

            st = []

            for i in range(n):

                while st and arr[st[-1]]>arr[i]:

                    st.pop()

                pse[i] = st[-1] if st else -1
                st.append(i)

            return pse
        nse = findnse(arr)
        psee = findpsee(arr)

        total = 0
        MOD = 10**9 + 7
        for i in range(n):

            left = i - psee[i]
            right = nse[i] - i

            total = (total + left * right * arr[i]) % MOD

        return total