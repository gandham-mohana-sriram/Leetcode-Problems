class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=='(' or i=='['or i=='{':
                l.append(i)
            elif (len(l)>=1):
                if i=='}'and l.pop()!='{':
                    return False
                elif i==']'and l.pop()!='[':
                    return False
                elif i==')'and l.pop()!='(':
                    return False
            else:
                return False
        if(len(l)==0):
            return True
        else :
            return False


            
        