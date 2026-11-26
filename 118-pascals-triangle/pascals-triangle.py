class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l=[]
        for i in range(n):
            row=[0]*(i+1)
            for j in range(i+1):
                if j==0 or j==i:
                    row[j]=1
                else:
                    row[j]=p[j-1]+p[j]
            p=row;
            l.append(row)
        return l
