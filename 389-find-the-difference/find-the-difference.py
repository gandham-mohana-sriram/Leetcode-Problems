class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        su=0
        for i in range(len(t)):
            su+=ord(t[i])
        for i in range(len(s)):
            su-=ord(s[i])
        su = abs(su-0)
        return chr(su)
