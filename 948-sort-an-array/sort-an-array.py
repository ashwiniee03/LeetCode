class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def merge(a,b):
            i=0
            j=0
            res=[]
            while (i<len(a) and j<len(b)):
                if (a[i]<b[j]):
                    res.append(a[i])
                    i+=1
                else:
                    res.append(b[j])
                    j+=1

            res.extend(a[i:])
            res.extend(b[j:])
            return res

        def merge_sort(nums):
            if (len(nums)==1):
                return nums

            mid = len(nums)//2
            left= merge_sort(nums[:mid])
            right= merge_sort(nums[mid:])

            return merge(left,right)

        return merge_sort(nums)



        