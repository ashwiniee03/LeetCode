class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        INT32_MIN = -2**31
        INT32_MAX = 2**31 - 1
        n=x
        neg_flag= False
        if (n==0): return 0
        if (n<0):
            neg_flag= True
            n= n*(-1)
        
        rev_num=0
        while(n>0):
            d= n%10
            rev_num= rev_num*10+ d
            if (INT32_MAX< rev_num or rev_num< INT32_MIN): return 0
            n=n//10

        if (neg_flag):
            return rev_num*-1
        
        return rev_num
        
        