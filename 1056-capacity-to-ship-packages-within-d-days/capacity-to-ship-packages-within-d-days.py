def calculate_days(weights, mid):
    days=0
    w=0
    for weight in weights:
        if w+weight <= mid:
            w+= weight

        else:
            days+=1
            w= weight
    
    if w>0 and w<=mid:
        days+=1


    return days

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        low=max(weights)
        high= sum(weights)
        ans=0

        while (low<= high):
            mid= (low+high)//2
            
            mid_days= calculate_days(weights, mid)

            if (mid_days> days):
                low= mid+1

            else:
                high=mid-1
                ans= mid

        return ans

        