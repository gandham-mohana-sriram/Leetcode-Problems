class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l=[]
        for i in range(1000001):
            if i not in arr:
                l.append(i)
            if len(l)>k:
                break
        return l[k]