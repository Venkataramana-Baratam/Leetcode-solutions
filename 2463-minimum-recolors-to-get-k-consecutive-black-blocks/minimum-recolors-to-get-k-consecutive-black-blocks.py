class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mini = float('inf')  # Initialize mini with infinity
        
        # Iterate over each sliding window of size k
        for i in range(len(blocks) - k + 1):
            count = 0  # Reset count for each new window
            
            # Count 'W's in the current window
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    count += 1
            
            # Update mini after processing the entire window
            mini = min(mini, count)
        
        return mini
