class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        res = []

        for i in range(len(code)):
            if code[i] and code[i].isalnum() or '_' in code[i]:
                if businessLine[i] in order:
                    if isActive[i]:
                        res.append((order[businessLine[i]], code[i]))
        res.sort()

        ans = []
        for item in res:
            ans.append(item[1])
        return ans
