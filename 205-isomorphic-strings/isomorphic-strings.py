class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)!= len(t)):
            return False

        hash_one={}
        hash_two= {}
        i=0
        while i<len(s):
            if s[i] not in hash_one:
                if t[i] in hash_two:
                    return False
                else:
                    hash_one[s[i]] = t[i]
                    hash_two[t[i]] = s[i]

            else:
                if hash_one[s[i]]!=t[i]:
                    return False

            i+=1


        return True



        