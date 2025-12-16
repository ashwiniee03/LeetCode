class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        i=0
        j=i+1

        while(j<n):
            if (nums[i]==0):
                if (nums[j]!=0):
                    nums[i], nums[j]= nums[j], nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1

            else:
                i+=1
                j+=1        
        
        