class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        prefix= 1
        suffix= 1
        max_prod= float('-inf')

        for i in range(n):

            if prefix==0:
                prefix=1

            if suffix==0:
                suffix=1
                
            prefix*= nums[i]
            suffix*= nums[n-i-1]

            

            max_prod= max(max_prod, max(prefix, suffix))

        return max_prod