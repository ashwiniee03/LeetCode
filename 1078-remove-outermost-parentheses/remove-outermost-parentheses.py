class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        depth= 0 
        for i in s:
            if (i=="("):
                if depth>0:
                    ans+=i

                depth+=1

            else:
                if depth>1:
                    ans+=i

                depth-=1
                

        return ans