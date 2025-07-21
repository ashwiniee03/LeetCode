class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int ml= 1;
        int c=1;
        int n= nums.size();
        if (n==0) return 0;
        sort(nums.begin() , nums.end());
        for (int i=1 ; i<n; i++ ){
            if (nums[i]== nums[i-1]){
                continue;
            }
            if(nums[i]-1 == nums[i-1]){
                c++;
            }
            else{
                ml= max(ml, c);
                c=1;
                
            }
        }
        return max(ml, c);;
    }
};