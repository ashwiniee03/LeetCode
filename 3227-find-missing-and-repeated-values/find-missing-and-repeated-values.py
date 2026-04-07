class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n= len(grid)
        ans=[]
        n_n= n*n
        expected_sum= (n_n*(n_n+1))//2
        expected_sq_sum= (n_n *(n_n +1 )*((2* n_n)+1))//6

        actual_sum= 0
        actual_sq_sum= 0

        for i in grid:
            for j in i:
                actual_sum+= j
                actual_sq_sum+= j*j

        a_minus_b= actual_sum - expected_sum
        a_sq_minus_b_sq= actual_sq_sum -expected_sq_sum
        a_plus_b= a_sq_minus_b_sq // a_minus_b
        a= (a_minus_b + a_plus_b)//2
        b= a_plus_b -a

        return [a,b]



        