class Solution {
public:
    int maxDepth(string s) {
        // stack<char> st;
        int cnt=0,maxi=0;
        for(char ch:s){
            if(ch=='(') {
                // st.push(ch);
                cnt++;
                }
            else if(ch==')'){
            maxi = max(maxi, cnt);
            // st.pop();
            cnt--;
            }
            else continue;
        
        }
        return maxi;
    }
};