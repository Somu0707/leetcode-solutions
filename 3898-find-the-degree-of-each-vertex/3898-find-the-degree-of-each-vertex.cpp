class Solution {
public:
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        int m = matrix.size();
        vector<int> arr(m,0);
        for(int i=0;i<m;i++){
            for(int j=0;j<m;j++){
                if(matrix[i][j]==1) {
                    arr[i]++;
                    // arr[j]++;
                }
            }
        }
        return arr;
    }
};