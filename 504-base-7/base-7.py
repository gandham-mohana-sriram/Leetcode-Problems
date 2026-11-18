class Solution:
    def convertToBase7(self, num: int) -> str:
        n=abs(num)
        s=""
        if num==0:
            return '0'
        while(n>0):
            r=n%7
            s+=str(r)
            n=n//7
        s=s[::-1]
        if(num<0):
            s="-"+s
        return s