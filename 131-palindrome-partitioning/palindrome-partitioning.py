class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        res = []
        path = []
        def fun(index,s,res,path):
            if index == len(s):
                res.append(path[:])
                return 
            for i in range(index,len(s)):
                if ispalindrome(s,index,i):
                    path.append(s[index:i+1])
                    fun(i+1,s,res,path)
                    path.pop()
        def ispalindrome(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        fun(0,s,res,path)
        return res