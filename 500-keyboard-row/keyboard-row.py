class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        fi="qwertyuiop"
        mi="asdfghjkl"
        ti="zxcvbnm"
        l=[]
        for i in words:
            t=True
            for j in range(len(i)-1):
                if i[j].lower() in fi and i[j+1].lower() not in fi:
                    t=False
                    break
                elif i[j].lower() in mi and i[j+1].lower() not in mi:
                    t=False
                    break
                elif i[j].lower() in ti and i[j+1].lower() not in ti:
                    t=False
                    break
            if t==True:
                l.append(i)
        return l


                
