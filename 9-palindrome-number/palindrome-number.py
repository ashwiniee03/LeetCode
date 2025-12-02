class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):return False
        else:
            m=x
            rev=0
            while(x!=0):
                d= x%10
                rev= rev*10+d
                x=x//10
            if (m==rev): return True
            else: return False
        