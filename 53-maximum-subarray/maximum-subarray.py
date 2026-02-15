class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s=0
        max_sum= float('-inf')
        n= len(nums)

        for i in range (n):
            s+= nums[i]

            max_sum= max (s, max_sum)
            
            if (s<0):
                s=0

        return max_sum
        
                