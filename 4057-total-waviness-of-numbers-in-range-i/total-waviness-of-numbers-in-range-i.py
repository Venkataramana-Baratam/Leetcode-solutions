class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        

        total = 0

        for i in range(num1,num2+1):

            str_num = str(i)

            n = len(str_num)

            if n<=2:
                continue

            for j in range(1,n-1):

                a = str_num[j-1]
                b = str_num[j]
                c = str_num[j+1]

                if a < b > c:
                    total +=1
                elif a > b < c:
                    total+=1

        return total 