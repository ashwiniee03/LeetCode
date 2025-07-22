class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int row=n;
        int col=n;
        vector <vector <int>> matrix (row, vector <int>(col));

        int l=0;
        int r= col-1;
        int t=0;
        int b= row-1;
        int num=1;

        while(l<=r && t<=b && num<= (n*n)){
            for (int i=l; i<=r ; i++){
                matrix[t][i] = num++;
                
            }
            t++;


            for (int i=t; i<=b ; i++){
                matrix[i][r]= num++;
            }
            r--;


            if (t<=b){
                for (int i=r; i>=l ; i--){
                    matrix[b][i]= num++;
            }
            b--;
            }
            

            if (l<=r){
                for (int i=b; i>=t ; i--){
                    matrix[i][l]=num++;
            }
            l++;
            }
            
        }
        return matrix;
    }
};