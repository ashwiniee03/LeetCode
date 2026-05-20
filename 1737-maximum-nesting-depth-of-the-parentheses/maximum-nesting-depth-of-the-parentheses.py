class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        count=0
        for i in s:
            if i=='(':
                count+=1
                ans= max(count, ans)

            elif i==')':
                count-=1

        return ans
        