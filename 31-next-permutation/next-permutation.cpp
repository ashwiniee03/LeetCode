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
            int c=INT_MAX;
            int pos;
            for (int j= key+1 ; j<n; j++){
                if (nums[j]>nums[key] && nums[j]<c){
                    c= nums[j];
                    pos=j;
                }
            }
            swap(nums[key] , nums[pos]);
            sort(nums.begin()+key+1 , nums.end());
        }

        
    }
};