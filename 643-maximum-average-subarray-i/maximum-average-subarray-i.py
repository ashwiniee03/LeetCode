class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = float('-inf')
        start=0
        n= len(nums)
        s=0
        c=0
        j=0
        i=0

        while(j<n):
            
            if (c==k):
                if (s>max_sum):
                    max_sum=s
                    start=i

                s-=nums[i]
                c-=1
                i+=1

            else:
                s+= nums[j]
                c+=1
                j+=1

        if (c==k):
                if (s>max_sum):
                    max_sum=s
                    start=i

                s-=nums[i]
                c-=1
                i+=1

        return max_sum/float(k)

            







        