class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n= len(nums)
        arr= sorted(nums)
        j= n-1
        count =0

        for i in range(n):
            j= n-1

            while ((arr[i]+ arr[j]) >= target and j>i ):
                j-=1

            if (arr[i]+ arr[j] < target):
                count += j-i

        return count


        