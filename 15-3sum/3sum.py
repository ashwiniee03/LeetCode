class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        n= len(nums)
        nums.sort()

        for i in range(n):
            j= i+1
            k= n-1

            while(j<k):

                if (nums[j]+nums[k] > -1 * nums[i]):
                    k-=1

                elif (nums[j]+nums[k] < -1 * nums[i]):
                    j+=1

                else:
                    arr=[nums[i], nums[j], nums[k]]
                    if arr not in result:
                        result.append(arr)
                    j+=1
                    k-=1

        return result

