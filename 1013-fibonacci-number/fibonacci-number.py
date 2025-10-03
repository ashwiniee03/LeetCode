class Solution:
    def fib(self, n: int) -> int:
        f= []
        def helper(n:int):
            if (n<0):
                return
            
            helper(n-1)
            if (n==0 or  n==1):f.append(n)
            else: f.append(f[n-1]+f[n-2])
            

        helper(n)
        return f[n]

        