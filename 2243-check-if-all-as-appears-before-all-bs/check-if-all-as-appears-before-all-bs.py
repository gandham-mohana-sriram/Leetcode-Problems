class Solution:
    def checkString(self, s: str) -> bool:
        a=-1
        b=len(s)
        for i in range(len(s)):
            if s[i]=="a":
                a=i
            else:
                b=i
            if a>b:
                return False
        return True