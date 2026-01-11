class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        max_sum= -sys.maxsize -1
        current_sum= 0
        for i in nums:
            current_sum+= i
            max_sum= max(max_sum, current_sum)

            if (current_sum<0):
                current_sum= 0

        return max_sum
                