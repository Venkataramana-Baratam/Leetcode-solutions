class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []  
        for row in range(numRows):
            temp = [1] 
            if res:  
                last_row = res[-1]
                for j in range(1, len(last_row)):
                    temp.append(last_row[j - 1] + last_row[j])
                temp.append(1) 
            res.append(temp)

        return res
