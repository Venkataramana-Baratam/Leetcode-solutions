class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged={}
        for id1,val1 in nums1:
            if id1 in merged:
                merged[id1]+=val1
            else:
                merged[id1]=val1
        for id2,val2 in nums2:
            if id2 in merged:
                merged[id2]+=val2
            else:
                merged[id2]=val2
        result = [[id,merged[id]]for id in sorted(merged.keys())]
        return result 