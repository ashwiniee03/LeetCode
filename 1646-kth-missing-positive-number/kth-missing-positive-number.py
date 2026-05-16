def find_num(arr, num):
    low= 0
    high= len(arr)-1
    while(low<=high):
        mid=(low+high)//2

        if (arr[mid]==num):
            return True

        elif(arr[mid]>num):
            high= mid-1

        else:
            low= mid+1

    return False


class Solution(object):

    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        int_arr= []
        i=0
        n=1
        while(i<=k):
            if (find_num(arr,n)):
                n+=1
            else:
                int_arr.append(n)
                i+=1
                n+=1

        return int_arr[k-1]

        