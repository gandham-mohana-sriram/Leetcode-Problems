class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x)[2:]
        b=bin(y)[2:]
        width = max(len(a), len(b))
        a = a.zfill(width)
        b = b.zfill(width)
        c=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        return c