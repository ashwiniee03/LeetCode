class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()
        ans=[]
        i=0
        while i< len(strs[0]):
            if (strs[0][i]==strs[-1][i]):
                ans.append(strs[0][i])
            else:
                break
            i+=1

        return ''.join(ans)

        