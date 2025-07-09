class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st = []
        res = [-1]*n
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if len(st)==0:
                res[i] = -1
            else:
                res[i] = st[-1]
            st.append(nums2[i])
        temp = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    temp.append(j)
        ans = []
        for num in temp:
            ans.append(res[num])
        return ans
