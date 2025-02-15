class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_split_sum(num_str, target_sum):
            # Helper function to check if num_str can be split into parts that sum to target_sum
            if target_sum == 0 and not num_str:
                return True
            for i in range(1, len(num_str) + 1):
                part = int(num_str[:i])
                if part > target_sum:
                    break
                if can_split_sum(num_str[i:], target_sum - part):
                    return True
            return False

        total_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_split_sum(square_str, i):
                total_sum += i * i  
        return total_sum
