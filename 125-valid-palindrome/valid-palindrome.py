class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st=''
        for i in s:
            if (i.isalnum()):
                st+=i.lower()
            
        n= len (st)
        i=0
        j= n-1

        while(i<=j):
            if (st[i]== st[j]):
                i+=1
                j-=1
            else:
                return False

        return True
        