class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_dict= {0:0, 1:0, 2:0}
        n= len(nums)
        for i in nums:
            count_dict[i]= count_dict[i]+1
        
        j=0
        
        for i in count_dict:
            for k in range (count_dict[i]):
                nums[j]= i
                j+=1

        return nums



        