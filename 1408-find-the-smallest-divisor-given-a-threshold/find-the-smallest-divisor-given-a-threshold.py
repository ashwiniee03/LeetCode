def divisor_sum(nums, mid):
    ans=0
    for i in nums:
        ans += (i +mid -1)//mid

    return ans


class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        low= 1
        high= max(nums)
        ans=-1

        while(low<=high):
            mid= (low+high)//2

            div_sum= divisor_sum(nums, mid)

            if (div_sum> threshold):
                low= mid+1

            else:
                high= mid-1
                ans= mid

        return ans


        