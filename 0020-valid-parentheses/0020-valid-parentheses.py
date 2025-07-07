class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                it = stack[-1]
                stack.pop()
                if (s[i]== ')' and it == '(') or (s[i] == ']' and it == '[') or (s[i] == '}' and it =='{'):
                    continue
                else:
                    return False
        return len(stack)==0