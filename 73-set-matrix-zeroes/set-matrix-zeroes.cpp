class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int r= matrix.size();
        int c= matrix[0].size();
        vector <pair <int, int>> ind;

        for ( int i=0 ; i<r ; i++){
            for ( int j=0 ; j<c ; j++){
                if (matrix[i][j]==0){
                    ind.push_back({i,j});
                }
            }
        }
        for (auto [i,j] : ind){
            for (int k=0; k<c ; k++){
                matrix[i][k]=0;
            }

            for (int k=0; k<r ; k++){
                matrix[k][j]=0;
            }
        }
    }
};