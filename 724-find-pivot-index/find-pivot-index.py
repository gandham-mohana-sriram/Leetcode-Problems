class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s=sum(nums)
        su=0
        r=0
        for i in range(len(nums)):
            if i!=0:
                su+=nums[i-1]
            r=s-nums[i]-su
            if r==su:
                return i
        return -1
            
