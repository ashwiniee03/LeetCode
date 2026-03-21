class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n= len(nums)
        arr= sorted(nums)
        j= n-1
        count =0
        i=0

        while (i<j):
            if (arr[i]+arr[j]>=target):
                j-=1

            else:
                count+= j-i
                i+=1

        return count

        


        