class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        
        n = len(nums)
        total_sum = sum(nums)
        
        right_prod = [1] * n
        current_prod = 1
        

        for i in range(n - 1, -1, -1):
            right_prod[i] = current_prod
            

            if current_prod > total_sum:
                current_prod = total_sum + 1
            else:
                current_prod *= nums[i]
                
        sum_so_far = 0
        

        for i in range(n):
            if sum_so_far == right_prod[i]:
                return i
            
            sum_so_far += nums[i]
            
        return -1

        