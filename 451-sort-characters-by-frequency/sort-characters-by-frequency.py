class Solution(object):
    def frequencySort(self, s):

        d = {}
        ans =''

        for i in s:
            d[i] = d.get(i, 0) + 1

        buckets= [[] for _ in range(len(s))]

        for char, freq in d.items():
            buckets[freq-1].append(char)

        for i in range(len(s)-1, -1, -1):
            for ch in buckets[i]:
                ans+= ch * (i+1)

        return ans
        