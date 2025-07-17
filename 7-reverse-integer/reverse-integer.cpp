class Solution {
public:
    int reverse(int x) {
        long long  nn=0;
        int d;

    while(x!=0  ){
        d= x%10;

        nn= nn*10 +d;
        if ( !(INT_MIN<=nn &&  nn<= INT_MAX)){
            return 0;
        }

        x= x/10;
        
      }
    return nn;
    }
};