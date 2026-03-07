class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        check= s+s

        if (len(goal)!= len(s)):
            return False

        if (goal in check):
            return True

        
        return False