class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set= set(nums)
        count =0
        max_count= -1

        for i in nums_set:
            if (i-1 in nums_set):
                pass

            else:
                next_element= i+1
                count= 0
                while (next_element in nums_set):
                    count+=1
                    next_element+=1

                max_count= max(max_count, count)

        return max_count+1

                

        