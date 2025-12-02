class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        INT32_MIN = -2**31
        INT32_MAX = 2**31 - 1
        m= abs(x)
        neg_flag= False
   
        rev_num=0
        while(m>0):
            d= m%10
            rev_num= rev_num*10+ d
            if (INT32_MAX< rev_num or rev_num< INT32_MIN): return 0
            m=m//10

        if (x>0): return rev_num
        else: return (-1*rev_num)
        
        return rev_num
        
        