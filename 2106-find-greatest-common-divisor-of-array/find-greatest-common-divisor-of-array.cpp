class Solution {
public:
    int gcd(long long a, long long b){
        if (b==0){
            return a;
        }
        else return gcd(b, a%b);
    }

    int findGCD(vector<int>& nums) {
        long long s= *min_element(nums.begin(), nums.end());
        long long l= *max_element(nums.begin(), nums.end());
        
        return gcd(l,s);

    }
};