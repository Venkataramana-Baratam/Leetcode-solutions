class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        return all(count % 2 == 0 for count in frequency.values())