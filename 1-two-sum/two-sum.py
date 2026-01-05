class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]

        n= len(nums)
        hash_map= {}
        for i in range (n):
            hash_map[nums[i]]= i

        for i in range (n):
            key =target - nums[i]
            if ((key) in hash_map and i!= hash_map[key] ):
                ans.append(i)
                ans.append(hash_map[target - nums[i]])
                return ans

        