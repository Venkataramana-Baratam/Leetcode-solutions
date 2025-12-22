class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        def lower_bound(row, low, high, target):
            lb = len(row)
            while low <= high:
                mid = (low + high) // 2
                if row[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb

        def upper_bound(row, low, high, target):
            ub = len(row)
            while low <= high:
                mid = (low + high) // 2
                if row[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ub

        ans = 0
        max_ones = 0

        for i in range(len(mat)):
            row = mat[i]
            row.sort()   # ⭐ REQUIRED for binary search

            l = lower_bound(row, 0, len(row) - 1, 1)
            r = upper_bound(row, 0, len(row) - 1, 1)

            ones = r - l
            if ones > max_ones:
                max_ones = ones
                ans = i

        return [ans, max_ones]
