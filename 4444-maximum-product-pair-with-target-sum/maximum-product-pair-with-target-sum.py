class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        m=float('-inf')
        a,b=0,0
        for i in range(0,len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target and nums[i]>nums[j]):
                    if(nums[i]*nums[j]>=m):
                        a=i
                        b=j
                        m=nums[i]*nums[j]
                j+=1
        if(a==0 and b==0):
            return [-1,-1]
        return [a,b]       

        