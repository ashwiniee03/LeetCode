class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        max_c=0

        for i in nums:
            if (i==1):
                c+=1
            else:
                max_c= max(c, max_c)
                c=0
        max_c= max(c, max_c)
        return max_c
        