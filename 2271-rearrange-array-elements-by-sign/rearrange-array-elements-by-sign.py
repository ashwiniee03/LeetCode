class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_array= []
        negative_array= []
        ans=[]
        k=0
        n=len(nums)

        for i in range ((n)):
            if (nums[i]>0):
                positive_array.append(nums[i])

            else:
                negative_array.append(nums[i])


        while (k <n/2):
            ans.append(positive_array[k])
            ans.append(negative_array[k])
            k+=1

        return ans


        