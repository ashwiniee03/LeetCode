class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        sign=1
        i=0
        
        while i<len(s) and s[i]==' ':
            i+=1

        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        elif i < len(s) and s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1

        ans = sign * ans

        INT_MIN = -2**31
        INT_MAX =  2**31-1

        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX

        return ans


            