class Solution(object):
    def check(self, nums):
        n= len(nums)
        ans=0
        for i in range(n):
            if (nums[i]>nums[(i+1)%n]):
                ans+=1

        if (ans>1):
            return False
        else:
            return True

        