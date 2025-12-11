class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        arr = []
        for key in freq:
            arr.append([key, freq[key]])

        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):

                if arr[i][1] > arr[j][1]:
                    arr[i], arr[j] = arr[j], arr[i]

                elif arr[i][1] == arr[j][1] and arr[i][0] < arr[j][0]:
                    arr[i], arr[j] = arr[j], arr[i]
                
        result = []
        for val, count in arr:
            for _ in range(count):
                result.append(val)

        return result
