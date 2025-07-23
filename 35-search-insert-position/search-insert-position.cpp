class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int ans= nums.size();
        int l=0; int h= nums.size()-1;
        int mid;
        

        while(l<=h){
            mid = l + ((h-l)/2);

            if (nums[mid]>=target){
                ans=mid;
                h= mid-1;
            }
            else{
                l= mid+1;
            }
        }

        return ans;
        
    }
};