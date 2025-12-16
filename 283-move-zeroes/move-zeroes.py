class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        i= -1
        for k in range(n):
            if nums[k]==0:
                i=k
                break
        if (i<0): return
        j=i+1

        while (j<n):
            if(nums[j]!=0):
                nums[i], nums[j]= nums[j], nums[i]
                i+=1
                j+=1
            else:
                j+=1
        
        
        