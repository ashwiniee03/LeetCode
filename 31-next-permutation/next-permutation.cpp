class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int b=0;
        int n= nums.size();
        for (int i=n-1 ; i>0 ; i--){
            if (nums[i-1]<nums[i]){
                b=i;
                break;
            }
        }

        if(b==0){
            reverse(nums.begin() , nums.end());
        }else{
            int key= b-1;
            int c;
            int pos;
            for (int j= n-1 ; j>key ; j--){
                if (nums[j]>nums[key]){
                    c= j;
                    break;
                }
            }
            swap(nums[key] ,nums[c]);
            sort(nums.begin()+key+1 , nums.end());
        }

        
    }
};