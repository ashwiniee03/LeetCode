class Solution(object):
    def check(self, nums):
        ans=0
        for i in range(len(nums)-1):
            if (nums[i]>nums[i+1]):
                ans+=1

        if (nums[0]<nums[len(nums)-1]):
            ans+=1
        if (ans>1):
            return False
        else:
            return True

        