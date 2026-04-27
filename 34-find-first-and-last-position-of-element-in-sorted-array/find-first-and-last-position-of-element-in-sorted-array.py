class Solution(object):


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lowerBound( nums, target):
            low=0
            high= len(nums)-1
            ans=len(nums)

            while (low<= high):
                mid= (low+high)//2
                if (nums[mid]>=target):
                    ans=mid
                    high= mid-1

                else:
                    low= mid+1

            return ans

        def upperBound(nums, target):
            low=0
            high= len(nums)-1
            ans=len(nums)

            while (low<= high):
                mid= (low+high)//2
                if (nums[mid]>target):
                    ans=mid
                    high=mid-1

                else:
                    low=mid+1

            return ans
        


        l= lowerBound(nums, target)
        if ( l== len(nums) or nums[l]!= target ):
            return [-1, -1]

        u= upperBound(nums, target)
        return [l,u-1]

        
        