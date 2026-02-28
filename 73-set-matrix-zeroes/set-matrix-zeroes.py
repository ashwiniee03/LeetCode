class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix)
        n= len(matrix[0])

        top_row_zero=False
        top_column_zero=False

        for i in range(0,n):
            if matrix[0][i] ==0:
                top_row_zero=True

        for i in range(0,m):
            if matrix[i][0] ==0:
                top_column_zero=True

        for i in range(1,m):
            for j in range(1,n):
                if (matrix[i][j]==0):
                    matrix[0][j]=0
                    matrix[i][0]=0


        for i in range(1,n):
            if matrix[0][i]==0:
                for j in range(1,m):
                    matrix[j][i]=0

        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0

        if (top_row_zero):
            for i in range(0,n):
                matrix[0][i]=0

        if (top_column_zero):
            for i in range(0,m):
                matrix[i][0]=0

       




        