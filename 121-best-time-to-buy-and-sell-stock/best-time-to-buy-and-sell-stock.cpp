class Solution {
public:
    int maxProfit(vector<int>& prices) {
       
        int cp= prices[0];
        int profit=0;

        for(int i=1; i <prices.size(); i++){
            profit= max(profit , prices[i]- cp);
            cp= min(cp, prices[i]);
        }
        return profit;
    }
};