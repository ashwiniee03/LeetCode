class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        k=-1
        n=len(num)
        for i in range(n-1,-1,-1):
            if int(num[i])%2==1:
                k=i
                break

        return num[:k+1]

        


        
