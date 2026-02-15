class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        e=0
        n= len(nums)

        for i in range (n):
            if (c==0):
                c=1
                e=nums[i]

            else:
                if (nums[i]== e):
                    c+=1
                else:
                    c-=1

        return e

                