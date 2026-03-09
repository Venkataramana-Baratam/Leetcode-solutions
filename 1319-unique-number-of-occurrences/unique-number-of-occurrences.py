class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mpp = {}

        for num in arr:
            mpp[num] = mpp.get(num, 0) + 1

        counts = list(mpp.values())

        return len(counts) == len(set(counts))