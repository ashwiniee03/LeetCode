class Solution(object):
    

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l= s.split()
        ans= l[::-1]
        return " ".join(ans)




        