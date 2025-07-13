class Solution {
public:
    //Ashwini
    int maxSubArray(vector<int>& nums) {
        int n= nums.size();
        int sum=nums[0];
        int max_n=nums[0];

        for (int i=1; i<n; i++){
           sum= max(nums[i] , sum + nums[i]);
           max_n= max( sum , max_n);
            
        }

        return max_n;
        
    }
};