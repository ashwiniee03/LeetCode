class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ans= False
        if (x<0): return ans
        
        num= x
        rev_num=0
        while(x>0):
            d= x%10
            rev_num = rev_num*10+d
            x=x//10

        if (rev_num==num):
            return not(ans)
        else:
            return ans
        