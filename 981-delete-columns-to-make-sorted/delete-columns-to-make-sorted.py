class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        c=0
        for j in range(len(strs[0])):
            a='a'
            for i in range(len(strs)):
                if a<=strs[i][j]:
                    a=strs[i][j]
                else:
                    c+=1
                    break
        return c
            
