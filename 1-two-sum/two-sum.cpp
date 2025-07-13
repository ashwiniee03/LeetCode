class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n= nums.size();
        int i1; int i2;
        unordered_map <int, int> m;
        for (int i=0; i<n; i++){
            int rem= target-nums[i];
            if (m.find(rem)!=m.end()){
                i1=i;
                i2= m[rem];
                break;
            }
            m[nums[i]]= i;
        }
        vector <int> ans= {i1, i2};
        return ans;
    }
};