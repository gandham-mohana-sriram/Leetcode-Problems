class Solution:
    def longestCommonPrefix(self, strs: l[str]) -> str:
        a=0
        ma=len(strs[0])
        for i in range(len(strs)):
            if(len(strs[i])<=ma):
                ma=len(strs[i])
                a=i
        b=strs[a]
        s=""
        r=""
        for i in range(len(b)):
            s+=b[i]
            a=0
            for j in range(len(strs)):
                if(strs[j].find(s)==0):
                    a+=1
            if(a==len(strs)):
                r+=b[i]
            else:
                return r
        return r   




