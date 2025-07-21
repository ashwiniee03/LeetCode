class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int r= matrix.size();
        int c=r;

        for (int i=0; i<r; i++){
            for (int j=0 ; j<r; j++){
                if (i>j){
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        for (auto &e: matrix){
            reverse(e.begin() , e.end());
        }
    }
};