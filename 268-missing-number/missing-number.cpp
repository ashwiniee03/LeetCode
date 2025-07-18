class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans=0;
        for (auto e :nums){
            ans=ans^e;
        }
        int n= nums.size();
        for (int i=0; i<=n; i++){
            ans^=i;
        }

        return ans;
    }    

    
};