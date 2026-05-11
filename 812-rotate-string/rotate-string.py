class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        


        if len(s)!=len(goal):
            return False

        def fun(ind):

            temp = s[n-ind:] + s[:n - ind]

            return temp
        i  = 0
        n = len(s)
        while i<n:
            if fun(i) == goal:
                return True
            i+=1
        return False


