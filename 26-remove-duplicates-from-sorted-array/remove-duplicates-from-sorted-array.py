class Solution(object):
    def removeDuplicates(self, nums):
        n= len(nums)
        p1=0
        p2=1
        while(p2< n):
            if (nums[p1]!= nums[p2]):
                nums[p1+1]= nums[p2]
                p1+=1
                p2+=1
            else:
                p2+=1
        return p1+1

        