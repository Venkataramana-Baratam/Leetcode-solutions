class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mini = float('inf')  
        for i in range(len(blocks) - k + 1):
            count = 0 
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    count += 1
            mini = min(mini, count)
        return mini
