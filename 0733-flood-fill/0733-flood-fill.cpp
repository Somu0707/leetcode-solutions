class Solution {
public:

    void dfs(vector<vector<int>> &image, int r, int c, int old, int color){
        int m = image.size();
        int n = image[0].size();
        if(r<0 || c<0 || r>=m || c>=n) return;
        if(image[r][c] != old) return;
        image[r][c] = color;
        dfs(image, r+1,c,old,color);
        dfs(image, r-1,c,old,color);
        dfs(image, r,c+1,old,color);
        dfs(image, r,c-1,old,color);
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int oldcolor = image[sr][sc];
        if(oldcolor == color) return image;
        dfs(image, sr, sc, oldcolor, color);
        return image;
    }
};