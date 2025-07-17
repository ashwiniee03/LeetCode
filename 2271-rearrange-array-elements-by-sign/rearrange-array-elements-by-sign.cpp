class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int i=0;
        int j=1;
        int n= nums.size();
        vector <int> ans (n);
        //Ashwini
        
        for (int k=0; k<n; k++){
            if (nums[k]>0){
                if (i<n){
                    ans[i]=nums[k];
                    i+=2;
                }
            }else{
                if (j<n){
                    ans[j]= nums[k];
                    j+=2;
                }
            }
        }

        return ans;
    }
};