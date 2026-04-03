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
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j= i+1
            k= n-1

            while(j<k):

                if (nums[j]+nums[k] > -1 * nums[i]):
                    k-=1

                elif (nums[j]+nums[k] < -1 * nums[i]):
                    j+=1

                else:
                    arr=[nums[i], nums[j], nums[k]]
                    result.append(arr)
                    j+=1
                    k-=1
                    while j  < k and nums[j] == nums[j- 1]:
                        j += 1
                    # Skip duplicates for right
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result

