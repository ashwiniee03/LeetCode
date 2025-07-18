class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int n1= nums1.size();
        int n2= nums2.size();
        int j=0;int k=0;
        vector <int> inter;
        int f=0;
        for (int i=0; i<n1; i++){
            j=k;
            while(j<n2){
                if (nums1[i]== nums2[j]){
                    if (inter.empty() || inter.back() != nums1[i]) {
                        inter.push_back(nums1[i]);
                    }
                    
                    k=j+1;
                }
                j++;
            }
            
        }
        return inter;
    }
};