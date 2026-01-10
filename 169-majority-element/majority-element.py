class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ch=nums[0]      
        c= 1

        for i in range (1, len (nums)):
            if (ch== nums[i]):
                c+=1 
            
            if (ch != nums[i]):
                if (c>0):
                    c-=1
                else:
                    c=1
                    ch=nums[i]

        return ch

                