class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix= {0:1}
        current_sum= 0
        count=0

        for i in range(len(nums)):
            current_sum+=nums[i]

            rem= current_sum-k

            if rem in prefix:
                count+=prefix[rem]

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return count