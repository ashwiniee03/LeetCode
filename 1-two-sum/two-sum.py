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
            rem=target-nums[i]
            if rem in hash_map:
                ans.append(i)
                ans.append(hash_map[rem])
                return ans

            hash_map[nums[i]] = i

            

        