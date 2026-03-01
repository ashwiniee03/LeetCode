class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m= len(matrix)
        n= len(matrix[0])
        ans=[]

        l= 0
        r= n-1
        t=0
        b= m-1

        while (l<=r and t<=b):
            for i in range(l, r+1):
                ans.append(matrix[t][i])

            for i in range(t+1, b+1):
                ans.append(matrix[i][r])

            if (t<b):

                for i in range (r-1, l-1, -1):
                    ans.append(matrix[b][i])

            if(l<r):
                for i in range( b-1, t, -1):
                    ans.append(matrix[i][l])

            l+=1
            r-=1
            t+=1
            b-=1

        return ans
        