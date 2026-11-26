class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n=len(columnTitle)
        su=0
        i=0
        while(n>0):
            n-=1
            p=26**n
            su+=p*(s.index(columnTitle[i])+1)
            i+=1
        return su