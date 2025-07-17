class Solution {
public:
    bool isPalindrome(string s) {
         
        string r="";
        
        
        for (char c: s){
            if (isalnum(c) && c!= ' ') r+= tolower(c);
        }

        int n= r.length();

        for (int i=0; i< n/2; i++){
            if(r[i]!= r[n-i-1]){
                return false;
            }
           
        }

        return true;
    }
};