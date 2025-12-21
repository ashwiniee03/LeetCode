class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n= len (nums)
        sum_of_nums= (n*(n+1))/2
        sum=0

        for i in nums:
            sum+=i
        
        return (sum_of_nums - sum)
        