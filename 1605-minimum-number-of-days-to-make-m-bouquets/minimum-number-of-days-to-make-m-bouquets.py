def no_of_boquets(mid, bloomDay,k):
    count=0
    ans=0
    for i in bloomDay:
        if (i<=mid):
            count+=1
        else:
            ans+= count//k
            count=0

    ans+= count//k

    return ans


class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n= len(bloomDay)
        if (m*k > n):
            return -1

        low= min(bloomDay)
        high= max(bloomDay)
        day= -1

        while (low<=high):
            mid= (low+high)//2

            no_boquets= no_of_boquets(mid, bloomDay,k)

            if no_boquets >= m:
                day = mid
                high = mid - 1
            else:
                low = mid + 1

        return day
