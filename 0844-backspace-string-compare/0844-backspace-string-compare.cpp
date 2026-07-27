class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // if(s.length()!=s.length()) return false;
        stack<char> st1;
        stack<char> st2;
        for(char ch:s){
            if(ch=='#'){
                if(!st1.empty()) st1.pop();
            }
            else st1.push(ch);
        }
        for(char ch:t){
            if(ch=='#'){
                if(!st2.empty()) st2.pop();
            }
            else st2.push(ch);
        }
        
        while(!st1.empty() && !st2.empty()){
            if(st1.top()!=st2.top()) return false;
            st1.pop();
            st2.pop();
        }
        if(st1.empty() && st2.empty()) return true;
        else return false;
        
    }
};