class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        i=-1
        for k in range(n):
            if nums[k]==0:
                i=k
                break

        if (i==-1): return
        
        for k in range(i+1,n):
            if (nums[k]!=0):
                nums[k], nums[i]= nums[i], nums[k]
                i+=1
            

        
        
        