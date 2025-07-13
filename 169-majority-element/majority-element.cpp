class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans;
        unordered_map <int, int> hash;
        int n= nums.size();
        for (int i=0; i<n; i++){
            hash[nums[i]]++;
        }

        for (auto it: hash){
            if (it.second > (n/2)){
                ans= it.first;
                break;
            }
        }

        return ans;

    }
};