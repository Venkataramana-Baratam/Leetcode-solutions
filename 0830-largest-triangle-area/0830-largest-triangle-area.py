class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]
                    area = abs(x1*(y2 - y3) +x2*(y3 - y1) +x3*(y1 - y2)) / 2.0
                    if area>max_area:
                        max_area = area
        return max_area