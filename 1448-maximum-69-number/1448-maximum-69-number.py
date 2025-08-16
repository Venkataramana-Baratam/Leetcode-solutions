class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = []
        temp = str(num)
        for i in temp:
            ans.append(i)
        maxi = 0
        res = ""
        for i in range(len(ans)):
            if ans[i]=='6':
                ans[i] = '9'
                break
        res = ''.join(ans)
        return int(res)