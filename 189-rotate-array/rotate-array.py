class Solution(object):
    

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def rotate_array(arr, i , j):
            while (i<=j):
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
                j-=1

        n=len (nums)
        k= k%n

        rotate_array(nums,0,n-k-1)
        rotate_array(nums,n-k,n-1)
        rotate_array(nums,0,n-1)

        return nums
        