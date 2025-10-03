class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        def helper(start:int, end:int):
            if (start>=end):
                return True
            if (s[start]!= s[end]):
                return False

            return helper(start+1, end-1)

        return helper(0, len(s)-1)
        def helper(start:int, end:int):
            if (start>=end):
                return True
            if (s[start]!= s[end]):
                return False

            return helper(start+1, end-1)

        return helper(0, len(s)-1)