class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(1,numRows+1):
            arr=[0]*i
            arr[0]=1
            arr[i-1]=1

            for j in range(1, i-1):
                arr[j]= result[i-2][j-1] + result[i-2][j]
            result.append(arr)

        return result

