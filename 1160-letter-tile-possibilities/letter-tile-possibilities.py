class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Track frequency of each uppercase letter (A-Z)
        char_count = [0] * 26
        for i in tiles:
            char_count[ord(i) - ord("A")] += 1  # Count each character
        
        return self.find_sequence(char_count)  # Start recursion with the character counts

    def find_sequence(self, char_count: list) -> int:
        total = 0

        # Try using each available character
        for pos in range(26):
            if char_count[pos] == 0:
                continue  # Skip characters with no remaining count

            # Add current character and recurse
            total += 1  # Count this as a valid sequence
            char_count[pos] -= 1  # Choose the current character (decrement its count)
            
            # Recursive call to explore the rest of the sequence
            total += self.find_sequence(char_count)

            # Backtrack: restore the character count after recursion
            char_count[pos] += 1  # Undo the choice (increment the count back)

        return total  # Return the total number of possibilities
