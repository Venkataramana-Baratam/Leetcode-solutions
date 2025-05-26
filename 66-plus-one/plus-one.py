class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        for  i in digits:
            ans.append(str(i))
        result  = "".join(ans)
        result = int(result)
        y = result+1
        y = str(y)
        ans1 =[]
        for i in y:
            ans1.append(int(i))
        return ans1