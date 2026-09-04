class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        prefix_sum = 0

        hash_map = {0:1}
        res = 0
        for num in nums:

            prefix_sum+=num

            if prefix_sum - k in hash_map:

                res+=hash_map[prefix_sum - k]

            hash_map[prefix_sum] = hash_map.get(prefix_sum , 0) + 1

        return res