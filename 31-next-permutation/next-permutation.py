def reverse_array(nums, start, end):
        while(start<end):
             nums[start], nums[end]= nums[end], nums[start]
             start+=1
             end-=1

        return nums

class Solution(object):
     



    def nextPermutation( self,nums):
            """
            :type nums: List[int]
            :rtype: None Do not return anything, modify nums in-place instead.
            """
            n= len (nums)
            pivot = -1
            

            for i in range (n-1 , 0, -1):
                if (nums[i-1]<nums[i]):
                    pivot= i-1
                    break

            print(pivot)

            if (pivot == -1):
                return reverse_array(nums, 0, n-1)

            for i in range (n-1 , -1, -1):
                if (nums[i]> nums[pivot]):
                    nums[i], nums[pivot]= nums[pivot], nums[i]
                    break

            nums= reverse_array(nums,pivot+1, n-1)
            return nums


        
        