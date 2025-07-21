class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set <int> set;
        if (nums.size()==0){return 0;}
        for (auto e: nums){
            set.insert(e);
        }

        int l=1;
        int c=1;

        for (auto e: set){
            c=1;
            if (set.find(e-1)== set.end()){
                int x= e;
                while (set.find(x+1)!= set.end()){
                    c++;
                    x++;
                }
            }
            l= max(l,c);
        }

        return l;
    }
};