import math

def calculate_hours(piles, mid):
        h=0
        for i in piles:
            h += (i + mid - 1) // mid

        return h


class Solution(object):
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        high= max(piles)
        low=1
        ans= float('inf')

        while(low<=high):
            mid= (low+high)//2

            hour= calculate_hours(piles, mid)
            if (hour> h):
                low= mid+1

            else:
                high= mid-1
                ans= mid

        return ans

            
        