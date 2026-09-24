class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=nums[i]
            s=0
            while(a>0):
                r=a%10
                s+=r
                a=a//10
            if(s==i):
                return i
        return -1
            