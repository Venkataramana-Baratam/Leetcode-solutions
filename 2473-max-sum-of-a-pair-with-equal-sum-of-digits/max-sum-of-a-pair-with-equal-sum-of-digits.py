from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum=-1
        mpp=defaultdict(int)
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum in mpp:
                max_sum = max(max_sum,num+mpp[digit_sum])
            mpp[digit_sum] = max(mpp[digit_sum],num)
        return max_sum