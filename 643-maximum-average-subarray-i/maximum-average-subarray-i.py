class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)
        p=0
        window_sum = sum(nums[:k])
        max_sum=window_sum
        for i in range (k,n):

            window_sum-= nums[p]
            p+=1
            window_sum+=  nums[i]

            max_sum= max(max_sum, window_sum)

        return max_sum/float(k)