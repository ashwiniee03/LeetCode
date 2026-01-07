class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        hash_map={}
        for i in range (n):
            hash_map[nums[i]]= hash_map.get(nums[i], 0)+1

        for i in range (n):
            if ((hash_map[nums[i]])> (n/2)):
                return nums[i]        