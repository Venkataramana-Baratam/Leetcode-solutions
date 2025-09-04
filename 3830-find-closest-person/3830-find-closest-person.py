class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_difference = abs(z - x)
        y_difference = abs(z - y)
        
        if x_difference < y_difference:
            return 1   
        elif y_difference < x_difference:
            return 2   
        else:
            return 0   
