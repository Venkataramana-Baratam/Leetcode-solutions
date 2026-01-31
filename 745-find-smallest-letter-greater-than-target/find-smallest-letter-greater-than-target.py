class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini = 123
        for letter in letters:
            if ord(letter)>ord(target):
                mini = min(ord(letter),mini)
        return chr(mini) if mini!=123 else letters[0]