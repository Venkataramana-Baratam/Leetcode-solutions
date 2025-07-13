class Solution:
    def processStr(self, s: str) -> str:
        result =[]
        for i in s:
            if i>='a' and i<='z':
                result.append(i)
            elif i=='*' and result:
                result.pop()
            elif i=='#' and result:
                result.extend(result[:])
            elif i=='%':
                result.reverse()
        return ''.join(result)